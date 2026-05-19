export type StudyMode = 'flashcards' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface SayingPage {
  id: string;
  pageNumber: number;
  subtitle: string;
  sayings: SayingData[];
}

export interface SayingData {
  saying: string;
  meaning: string;
  example: string;
}