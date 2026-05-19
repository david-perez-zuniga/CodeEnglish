export type StudyMode = 'flashcards' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface VerbPage {
  id: string;
  pageNumber: number;
  subtitle: string;
  isIrregular?: boolean;
  verbs: VerbData[];
}

export interface VerbData {
  base: string;
  pastSimple: string;
  pastParticiple: string;
  spanish: string;
}