export type StudyMode = 'flashcards' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface SynonymPage {
  id: string;
  pageNumber: number;
  subtitle: string;
  synonyms: SynonymData[];
}

export interface SynonymData {
  word: string;
  synonym: string;
}