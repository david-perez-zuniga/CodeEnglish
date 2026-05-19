import type { SynonymPage } from './types';

export const pagesData: SynonymPage[] = [
  { id: 'page-46', pageNumber: 46, subtitle: 'Synonyms', synonyms: [{ word: 'Fix', synonym: 'Resolve' }, { word: 'Build', synonym: 'Construct' }] },
  { id: 'page-47', pageNumber: 47, subtitle: 'Synonyms', synonyms: [{ word: 'Change', synonym: 'Modify' }, { word: 'Start', synonym: 'Initiate' }] },
  { id: 'page-48', pageNumber: 48, subtitle: 'Synonyms', synonyms: [{ word: 'Find', synonym: 'Discover' }, { word: 'Save', synonym: 'Preserve' }] },
  { id: 'page-49', pageNumber: 49, subtitle: 'Synonyms', synonyms: [{ word: 'Test', synonym: 'Verify' }, { word: 'Fix', synonym: 'Repair' }] },
  { id: 'page-50', pageNumber: 50, subtitle: 'Synonyms', synonyms: [{ word: 'Help', synonym: 'Assist' }, { word: 'End', synonym: 'Conclude' }] },
  { id: 'page-51', pageNumber: 51, subtitle: 'Synonyms', synonyms: [{ word: 'Think', synonym: 'Consider' }, { word: 'Create', synonym: 'Develop' }] },
];

export const STUDY_MODES = ['flashcards', 'speaking', 'writing'] as const;