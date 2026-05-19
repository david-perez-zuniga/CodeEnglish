export type StudyMode = 'flashcards' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface IdiomPage {
  id: string;
  pageNumber: number;
  subtitle: string;
  idioms: IdiomData[];
}

export interface IdiomData {
  phrase: string;
  meaning: string;
  example: string;
}