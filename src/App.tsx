import React, { useState, FormEvent, useRef, useEffect } from 'react';
import { Send, Play, Bot, User, ChevronDown, ChevronUp, AlertCircle } from 'lucide-react';

interface Arguments {
  param: Record<string, any>;
  data: Record<string, any>;
}

interface MetaData {
  data: Record<string, any>;
  param: Record<string, any>;
  req_type: string;
  url: string;
}

interface AskResponse {
  meta_data: MetaData;
  success: boolean;
  tool_name: string;
  error?: string;
}

interface ExecuteResponse {
  result: string;
  success: boolean;
  error?: string;
}

interface Message {
  type: 'user' | 'bot';
  content: string;
  response?: AskResponse;
  executeResponse?: ExecuteResponse;
  editedMetaData?: MetaData;
  error?: boolean;
}

function App() {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<Message[]>([
    {
      type: 'bot',
      content: 'Welcome to PingFederate Admin API Assistant! How can I help you today?'
    }
  ]);
  const [isLoading, setIsLoading] = useState(false);
  const [expandedSections, setExpandedSections] = useState<Record<string, boolean>>({});
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    const userMessage: Message = {
      type: 'user',
      content: query
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);
    setQuery('');

    try {
      const res = await fetch('http://127.0.0.1:5000/ask_gpt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query
        }),
      });

      if (!res.ok){
        console.log("query : ",query);
        throw new Error('Failed to get response');
      }       
      const data: AskResponse = await res.json();
      const botMessage: Message = {
        type: 'bot',
        content: data.success ? 'I found a relevant tool that might help:' : `Error: ${data.error || 'An unexpected error occurred'}`,
        response: data,
        editedMetaData: data.success ? { ...data.meta_data } : undefined,
        error: !data.success
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      const errorMessage: Message = {
        type: 'bot',
        content: `Error: ${err instanceof Error ? err.message : 'An error occurred'}`,
        error: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleExecute = async (toolName: string, messageIndex: number) => {
    const message = messages[messageIndex];
    if (!message.editedMetaData) return;

    setIsLoading(true);

    try {
      const res = await fetch('http://127.0.0.1:5000/execute_tool', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          tool_name: toolName,
          arguments: {
            param: message.editedMetaData.param,
            data: message.editedMetaData.data
          }
        }),
      });

      if (!res.ok) throw new Error('Failed to execute tool');
      const data: ExecuteResponse = await res.json();

      const executionMessage: Message = {
        type: 'bot',
        content: data.success ? 'Tool execution result:' : `Error: ${data.error || 'Tool execution failed'}`,
        executeResponse: data,
        error: !data.success
      };

      setMessages(prev => [...prev, executionMessage]);
    } catch (err) {
      const errorMessage: Message = {
        type: 'bot',
        content: `Error: ${err instanceof Error ? err.message : 'An error occurred'}`,
        error: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const isObjectEmpty = (obj: Record<string, any>) => {
    return Object.keys(obj).length === 0;
  };

  const updateJsonValue = (
    messageIndex: number,
    section: 'param' | 'data',
    path: string[],
    value: string
  ) => {
    setMessages(prev => {
      const newMessages = [...prev];
      const message = newMessages[messageIndex];
      if (!message.editedMetaData) return prev;

      let current = { ...message.editedMetaData };
      let target = current[section];
      const pathCopy = [...path];
      const lastKey = pathCopy.pop();

      if (!lastKey) return prev;

      let currentObj = target;
      for (const key of pathCopy) {
        currentObj[key] = { ...currentObj[key] };
        currentObj = currentObj[key];
      }

      try {
        currentObj[lastKey] = JSON.parse(value);
      } catch {
        currentObj[lastKey] = value;
      }

      message.editedMetaData = {
        ...message.editedMetaData,
        [section]: target
      };

      return newMessages;
    });
  };

  const renderJsonEditor = (
    data: Record<string, any>,
    messageIndex: number,
    section: 'param' | 'data',
    path: string[] = []
  ) => {
    return Object.entries(data).map(([key, value]) => {
      const currentPath = [...path, key];
      const isObject = value !== null && typeof value === 'object';

      return (
        <div key={currentPath.join('.')} className="space-y-2">
          {isObject ? (
            <div className="border-l-2 border-gray-200 pl-3 ml-2">
              <div className="text-sm font-medium text-gray-700 mb-2">{key}:</div>
              {renderJsonEditor(value, messageIndex, section, currentPath)}
            </div>
          ) : (
            <div className="flex gap-2 items-center">
              <span className="text-gray-600 font-medium min-w-[120px]">{key}:</span>
              <input
                type="text"
                value={JSON.stringify(value)}
                onChange={(e) => updateJsonValue(messageIndex, section, currentPath, e.target.value)}
                className="flex-1 px-2 py-1 rounded border border-gray-300 bg-white hover:bg-gray-50 focus:bg-white text-sm font-mono focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          )}
        </div>
      );
    });
  };

  const toggleSection = (messageId: number, section: string) => {
    setExpandedSections(prev => ({
      ...prev,
      [`${messageId}-${section}`]: !prev[`${messageId}-${section}`]
    }));
  };

  const isSectionExpanded = (messageId: number, section: string) => {
    return expandedSections[`${messageId}-${section}`] ?? false;
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <div className="max-w-4xl mx-auto h-screen flex flex-col">
        {/* Header */}
        <div className="bg-white border-b p-4 flex items-center gap-3">
          <Bot className="w-8 h-8 text-blue-600" />
          <h1 className="text-2xl font-bold text-gray-800">AI Agent</h1>
        </div>

        {/* Messages Container */}
        <div className="flex-1 overflow-y-auto p-4 space-y-4">
          {messages.map((message, index) => (
            <div key={index} className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`flex gap-3 max-w-[80%] ${message.type === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                <div className={`w-8 h-8 rounded-full flex items-center justify-center flex-shrink-0 ${
                  message.type === 'user' ? 'bg-blue-600' : message.error ? 'bg-red-600' : 'bg-gray-600'
                }`}>
                  {message.type === 'user' ? (
                    <User className="w-5 h-5 text-white" />
                  ) : message.error ? (
                    <AlertCircle className="w-5 h-5 text-white" />
                  ) : (
                    <Bot className="w-5 h-5 text-white" />
                  )}
                </div>
                <div className="space-y-2">
                  <div className={`p-4 rounded-lg ${
                    message.type === 'user' 
                      ? 'bg-blue-600 text-white' 
                      : message.error
                      ? 'bg-red-50 border border-red-200 text-red-800'
                      : 'bg-white shadow-md'
                  }`}>
                    <p>{message.content}</p>
                  </div>

                  {message.response && message.response.success && (
                    <div className="bg-white rounded-lg shadow-md p-4 space-y-3">
                      <div className="grid grid-cols-2 gap-3">
                        <div className="bg-gray-50 p-3 rounded">
                          <p className="text-sm font-medium text-gray-500">Tool Name</p>
                          <p className="font-semibold">{message.response.tool_name}</p>
                        </div>
                        <div className="bg-green-50 p-3 rounded">
                          <p className="text-sm font-medium text-green-700">Status</p>
                          <p className="font-semibold text-green-800">Ready to Execute</p>
                        </div>
                      </div>
                      
                      <div className="bg-gray-50 p-3 rounded">
                        <div className="grid grid-cols-2 gap-2 text-sm mb-3">
                          <div>
                            <p className="text-gray-500">Request Type</p>
                            <p className="font-medium">{message.response.meta_data.req_type}</p>
                          </div>
                          <div>
                            <p className="text-gray-500">URL</p>
                            <p className="font-medium break-all">{message.response.meta_data.url}</p>
                          </div>
                        </div>

                        {message.editedMetaData && !isObjectEmpty(message.editedMetaData.param) && (
                          <div className="border-t border-gray-200 pt-3">
                            <button
                              onClick={() => toggleSection(index, 'param')}
                              className={`flex items-center gap-2 text-sm font-medium transition-colors ${
                                isSectionExpanded(index, 'param')
                                  ? 'text-blue-600'
                                  : 'text-gray-500 hover:text-blue-600'
                              }`}
                            >
                              {isSectionExpanded(index, 'param') ? (
                                <ChevronUp className="w-4 h-4" />
                              ) : (
                                <ChevronDown className="w-4 h-4" />
                              )}
                              Parameters
                            </button>
                            {isSectionExpanded(index, 'param') && (
                              <div className="mt-2 space-y-2">
                                {renderJsonEditor(message.editedMetaData.param, index, 'param')}
                              </div>
                            )}
                          </div>
                        )}

                        {message.editedMetaData && !isObjectEmpty(message.editedMetaData.data) && (
                          <div className="border-t border-gray-200 pt-3">
                            <button
                              onClick={() => toggleSection(index, 'data')}
                              className={`flex items-center gap-2 text-sm font-medium transition-colors ${
                                isSectionExpanded(index, 'data')
                                  ? 'text-blue-600'
                                  : 'text-gray-500 hover:text-blue-600'
                              }`}
                            >
                              {isSectionExpanded(index, 'data') ? (
                                <ChevronUp className="w-4 h-4" />
                              ) : (
                                <ChevronDown className="w-4 h-4" />
                              )}
                              Data
                            </button>
                            {isSectionExpanded(index, 'data') && (
                              <div className="mt-2 space-y-2">
                                {renderJsonEditor(message.editedMetaData.data, index, 'data')}
                              </div>
                            )}
                          </div>
                        )}
                      </div>

                      <button
                        onClick={() => handleExecute(message.response.tool_name, index)}
                        className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 flex items-center gap-2 justify-center"
                        disabled={isLoading}
                      >
                        <Play className="w-4 h-4" />
                        Execute Tool
                      </button>
                    </div>
                  )}

                  {message.executeResponse && (
                    <div className={`rounded-lg shadow-md p-4 ${
                      message.error 
                        ? 'bg-red-50 border border-red-200 text-red-800' 
                        : 'bg-green-50 border border-green-200 text-green-800'
                    }`}>
                      <p>{message.executeResponse.result}</p>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-white rounded-lg shadow-md p-4">
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                  <div className="w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></div>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Form */}
        <div className="bg-white border-t p-4">
          <form onSubmit={handleSubmit} className="flex gap-2">
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Type your message here..."
              className="flex-1 px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
              disabled={isLoading}
            />
            <button
              type="submit"
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 flex items-center gap-2"
              disabled={isLoading || !query.trim()}
            >
              <Send className="w-4 h-4" />
              Send
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;