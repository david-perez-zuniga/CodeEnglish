import type { CountryPage } from './types';

export const pagesData: CountryPage[] = [
  { id: 'page-56', pageNumber: 56, subtitle: 'Countries & Nationalities', countries: [{ country: 'Brazil', adjective: 'Brazilian', person: 'a Brazilian' }, { country: 'Japan', adjective: 'Japanese', person: 'a Japanese' }] },
  { id: 'page-57', pageNumber: 57, subtitle: 'Countries & Nationalities', countries: [{ country: 'Germany', adjective: 'German', person: 'a German' }, { country: 'France', adjective: 'French', person: 'a French person' }] },
  { id: 'page-58', pageNumber: 58, subtitle: 'Countries & Nationalities', countries: [{ country: 'Italy', adjective: 'Italian', person: 'an Italian' }, { country: 'Spain', adjective: 'Spanish', person: 'a Spaniard' }] },
  { id: 'page-59', pageNumber: 59, subtitle: 'Countries & Nationalities', countries: [{ country: 'China', adjective: 'Chinese', person: 'a Chinese person' }, { country: 'India', adjective: 'Indian', person: 'an Indian' }] },
  { id: 'page-60', pageNumber: 60, subtitle: 'Countries & Nationalities', countries: [{ country: 'Canada', adjective: 'Canadian', person: 'a Canadian' }, { country: 'Australia', adjective: 'Australian', person: 'an Australian' }] },
];

export const STUDY_MODES = ['flashcards', 'speaking', 'writing'] as const;