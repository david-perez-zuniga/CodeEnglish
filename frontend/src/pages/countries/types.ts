export type StudyMode = 'flashcards' | 'speaking' | 'writing';
export type ViewState = 'selection' | 'study';

export interface CountryPage {
  id: string;
  pageNumber: number;
  subtitle: string;
  countries: CountryData[];
}

export interface CountryData {
  country: string;
  adjective: string;
  person: string;
}