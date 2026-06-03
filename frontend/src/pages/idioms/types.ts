export type StudyMode = 'flashcards' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface IdiomPage {
  id: number;
  pageNumber: number;
  subtitle: string;
}

export interface IdiomData {
  phrase: string;
  meaning: string;
  example: string;
}