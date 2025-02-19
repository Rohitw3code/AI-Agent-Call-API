import React, { useState, FormEvent, useRef, useEffect } from 'react';
import { Send, Play, Bot, User, ChevronDown, ChevronUp, AlertCircle, MessageSquare, Terminal, Cpu } from 'lucide-react';

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

interface BaseResponse {
  type: 'error' | 'ai-response' | 'result' | 'tool';
  error?: string;
}

interface ErrorResponse extends BaseResponse {
  type: 'error';
  error: string;
}

interface AIResponse extends BaseResponse {
  type: 'ai-response';
  ai: string;
}

interface ToolResponse extends BaseResponse {
  type: 'tool';
  tool_name: string;
  meta_data: MetaData;
}

interface ResultResponse extends BaseResponse {
  type: 'result';
  result: string;
  success: boolean;
}

type ApiResponse = ErrorResponse | AIResponse | ToolResponse | ResultResponse;

interface Message {
  type: 'user' | 'bot';
  content: string;
  responseType?: 'error' | 'ai-response' | 'result' | 'tool';
  toolData?: {
    name: string;
    metaData: MetaData;
  };
  result?: string;
  success?: boolean;
}

function App() {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<Message[]>([
    {
      type: 'bot',
      content: 'Welcome to PingFederate Admin API Assistant! How can I help you today?',
      responseType: 'ai-response'
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

      if (!res.ok) {
        throw new Error('Failed to get response');
      }

      const data: ApiResponse = await res.json();
      let botMessage: Message;

      switch (data.type) {
        case 'error':
          botMessage = {
            type: 'bot',
            content: `Error: ${data.error}`,
            responseType: 'error'
          };
          break;
        case 'ai-response':
          botMessage = {
            type: 'bot',
            content: data.ai,
            responseType: 'ai-response'
          };
          break;
        case 'tool':
          botMessage = {
            type: 'bot',
            content: 'I found a relevant tool that might help:',
            responseType: 'tool',
            toolData: {
              name: data.tool_name,
              metaData: data.meta_data
            }
          };
          break;
        default:
          botMessage = {
            type: 'bot',
            content: 'Received an unexpected response type',
            responseType: 'error'
          };
      }

      setMessages(prev => [...prev, botMessage]);
    } catch (err) {
      const errorMessage: Message = {
        type: 'bot',
        content: `Error: ${err instanceof Error ? err.message : 'An error occurred'}`,
        responseType: 'error'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleExecute = async (toolName: string, metaData: MetaData) => {
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
            param: metaData.param,
            data: metaData.data
          }
        }),
      });

      if (!res.ok) throw new Error('Failed to execute tool');
      const data: ResultResponse = await res.json();

      const executionMessage: Message = {
        type: 'bot',
        content: data.result,
        responseType: 'result',
        success: data.success
      };

      setMessages(prev => [...prev, executionMessage]);
    } catch (err) {
      const errorMessage: Message = {
        type: 'bot',
        content: `Error: ${err instanceof Error ? err.message : 'An error occurred'}`,
        responseType: 'error'
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const isObjectEmpty = (obj: Record<string, any>) => {
    return Object.keys(obj).length === 0;
  };

  const renderJsonEditor = (
    data: Record<string, any>,
    section: 'param' | 'data'
  ) => {
    return Object.entries(data).map(([key, value]) => {
      const isObject = value !== null && typeof value === 'object';

      return (
        <div key={key} className="space-y-2">
          {isObject ? (
            <div className="border-l-2 border-gray-200 pl-3 ml-2">
              <div className="text-sm font-medium text-gray-700 mb-2">{key}:</div>
              {renderJsonEditor(value, section)}
            </div>
          ) : (
            <div className="flex gap-2 items-center">
              <span className="text-gray-600 font-medium min-w-[120px]">{key}:</span>
              <div className="flex-1 px-3 py-2 rounded-lg bg-gray-50 text-sm font-mono text-gray-800">
                {JSON.stringify(value)}
              </div>
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

  const getMessageIcon = (message: Message) => {
    if (message.type === 'user') return <User className="w-5 h-5 text-white" />;
    
    switch (message.responseType) {
      case 'error':
        return <AlertCircle className="w-5 h-5 text-white" />;
      case 'tool':
        return <Terminal className="w-5 h-5 text-white" />;
      case 'result':
        return <Cpu className="w-5 h-5 text-white" />;
      default:
        return <Bot className="w-5 h-5 text-white" />;
    }
  };

  const getMessageStyle = (message: Message) => {
    if (message.type === 'user') {
      return 'gradient-bg text-white message-bubble user';
    }

    switch (message.responseType) {
      case 'error':
        return 'bg-red-50 border border-red-100 text-red-800 message-bubble error';
      case 'tool':
        return 'bg-indigo-50 border border-indigo-100 text-indigo-800 message-bubble bot';
      case 'result':
        return message.success 
          ? 'bg-green-50 border border-green-100 text-green-800 message-bubble bot'
          : 'bg-red-50 border border-red-100 text-red-800 message-bubble error';
      default:
        return 'bg-white border border-gray-100 message-bubble bot';
    }
  };

  const getAvatarStyle = (message: Message) => {
    if (message.type === 'user') return 'gradient-bg';
    
    switch (message.responseType) {
      case 'error':
        return 'bg-red-500';
      case 'tool':
        return 'bg-indigo-500';
      case 'result':
        return message.success ? 'bg-green-500' : 'bg-red-500';
      default:
        return 'bg-blue-500';
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-5xl mx-auto h-screen flex flex-col">
        {/* Header */}
        <div className="gradient-bg p-4 flex items-center gap-3 shadow-lg">
          <div className="bg-white/20 p-2 rounded-lg">
            <MessageSquare className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-white">PingFederate Assistant</h1>
            <p className="text-sm text-white/80">Powered by AI</p>
          </div>
        </div>

        {/* Messages Container */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6 scrollbar-hide">
          {messages.map((message, index) => (
            <div key={index} className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`flex gap-4 max-w-[85%] ${message.type === 'user' ? 'flex-row-reverse' : 'flex-row'}`}>
                <div className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 shadow-md ${getAvatarStyle(message)}`}>
                  {getMessageIcon(message)}
                </div>
                <div className="space-y-3">
                  <div className={`p-4 rounded-2xl shadow-sm ${getMessageStyle(message)}`}>
                    <p className="leading-relaxed">{message.content}</p>
                  </div>

                  {message.responseType === 'tool' && message.toolData && (
                    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-5 space-y-4">
                      <div className="grid grid-cols-2 gap-4">
                        <div className="bg-indigo-50 p-4 rounded-xl">
                          <p className="text-sm font-medium text-indigo-700 mb-1">Tool Name</p>
                          <p className="font-semibold text-indigo-900">{message.toolData.name}</p>
                        </div>
                        <div className="bg-blue-50 p-4 rounded-xl">
                          <p className="text-sm font-medium text-blue-700 mb-1">Status</p>
                          <p className="font-semibold text-blue-900">Ready to Execute</p>
                        </div>
                      </div>
                      
                      <div className="bg-gray-50 p-4 rounded-xl">
                        <div className="grid grid-cols-2 gap-4 text-sm mb-4">
                          <div>
                            <p className="text-gray-500 mb-1">Request Type</p>
                            <p className="font-medium text-gray-900">{message.toolData.metaData.req_type}</p>
                          </div>
                          <div>
                            <p className="text-gray-500 mb-1">URL</p>
                            <p className="font-medium text-gray-900 break-all">{message.toolData.metaData.url}</p>
                          </div>
                        </div>

                        {!isObjectEmpty(message.toolData.metaData.param) && (
                          <div className="border-t border-gray-200 pt-4">
                            <button
                              onClick={() => toggleSection(index, 'param')}
                              className="w-full flex items-center justify-between p-2 rounded-lg hover:bg-gray-100 transition-colors"
                            >
                              <span className="text-sm font-medium text-gray-700">Parameters</span>
                              {isSectionExpanded(index, 'param') ? (
                                <ChevronUp className="w-4 h-4 text-gray-500" />
                              ) : (
                                <ChevronDown className="w-4 h-4 text-gray-500" />
                              )}
                            </button>
                            {isSectionExpanded(index, 'param') && (
                              <div className="mt-3 space-y-3 px-2">
                                {renderJsonEditor(message.toolData.metaData.param, 'param')}
                              </div>
                            )}
                          </div>
                        )}

                        {!isObjectEmpty(message.toolData.metaData.data) && (
                          <div className="border-t border-gray-200 pt-4">
                            <button
                              onClick={() => toggleSection(index, 'data')}
                              className="w-full flex items-center justify-between p-2 rounded-lg hover:bg-gray-100 transition-colors"
                            >
                              <span className="text-sm font-medium text-gray-700">Data</span>
                              {isSectionExpanded(index, 'data') ? (
                                <ChevronUp className="w-4 h-4 text-gray-500" />
                              ) : (
                                <ChevronDown className="w-4 h-4 text-gray-500" />
                              )}
                            </button>
                            {isSectionExpanded(index, 'data') && (
                              <div className="mt-3 space-y-3 px-2">
                                {renderJsonEditor(message.toolData.metaData.data, 'data')}
                              </div>
                            )}
                          </div>
                        )}
                      </div>

                      <button
                        onClick={() => handleExecute(message.toolData!.name, message.toolData!.metaData)}
                        className="w-full px-4 py-3 gradient-bg text-white rounded-xl hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 flex items-center gap-2 justify-center transition-opacity"
                        disabled={isLoading}
                      >
                        <Play className="w-4 h-4" />
                        Execute Tool
                      </button>
                    </div>
                  )}
                </div>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-4">
                <div className="typing-indicator">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Form */}
        <div className="bg-white border-t p-4 shadow-lg">
          <form onSubmit={handleSubmit} className="flex gap-3 max-w-3xl mx-auto">
            <input
              ref={inputRef}
              type="text"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Type your message here..."
              className="flex-1 px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-sm"
              disabled={isLoading}
            />
            <button
              type="submit"
              className="px-6 py-3 gradient-bg text-white rounded-xl hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 flex items-center gap-2 transition-opacity shadow-sm"
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