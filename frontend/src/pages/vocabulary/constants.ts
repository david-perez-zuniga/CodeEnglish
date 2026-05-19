import type { Page, Word } from './types';

export const BOOK_PAGES: Page[] = Array.from({ length: 29 }, (_, i) => {
  const num = i + 1;
  if (num === 26) return { num, title: 'House & Furniture', desc: 'Page 26' };
  if (num === 27) return { num, title: 'Family', desc: 'Page 27' };
  if (num === 28) return { num, title: 'Body & Organs', desc: 'Page 28' };
  if (num === 29) return { num, title: 'Animals', desc: 'Page 29' };
  return { num, title: `Page ${num}`, desc: '~100 words' };
});

export const mockWords: Word[] = [
  { id: 1, word: 'Algorithm', translation: 'Algoritmo', example: 'The algorithm processes data efficiently.' },
  { id: 2, word: 'Database', translation: 'Base de datos', example: 'The database stores all user information.' },
  { id: 3, word: 'Function', translation: 'Función', example: 'This function returns a boolean value.' },
  { id: 4, word: 'Variable', translation: 'Variable', example: 'Declare a variable before using it.' },
];

export const STUDY_MODES = ['mixed', 'speaking', 'writing'] as const;