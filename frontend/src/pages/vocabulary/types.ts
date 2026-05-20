export type StudyMode = 'mixed' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface Word {
  id: number;
  word: string;
  translation: string;
  example: string;
}

export interface Page {
  num: number;
  title: string;
  desc: string;
}

export interface StudySessionResult {
  total: number;
  correct: number;
  incorrect: number;
  mode: StudyMode;
}