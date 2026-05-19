import type { IdiomPage } from './types';

export const pagesData: IdiomPage[] = [
  {
    id: 'page-41',
    pageNumber: 41,
    subtitle: 'Office Idioms',
    idioms: [
      { phrase: 'Call it a day', meaning: 'Terminar de trabajar por hoy', example: "We've fixed all the bugs, let's call it a day." },
      { phrase: 'Get the ball rolling', meaning: 'Comenzar un proyecto', example: "We need to get the ball rolling on this project." }
    ]
  },
  {
    id: 'page-42',
    pageNumber: 42,
    subtitle: 'Office Idioms',
    idioms: [
      { phrase: 'Think outside the box', meaning: 'Pensar creativamente', example: "We need to think outside the box to solve this." },
      { phrase: 'Hit the nail on the head', meaning: 'Acertar en algo', example: "You hit the nail on the head with that solution!" }
    ]
  },
  {
    id: 'page-43',
    pageNumber: 43,
    subtitle: 'Office Idioms',
    idioms: [
      { phrase: 'Play it by ear', meaning: 'Improvisar', example: "Let's play it by ear and see how the meeting goes." },
      { phrase: 'Take it easy', meaning: 'Relajarse', example: "After the deadline, I'm going to take it easy." }
    ]
  },
  {
    id: 'page-44',
    pageNumber: 44,
    subtitle: 'Office Idioms',
    idioms: [
      { phrase: 'Back to the drawing board', meaning: 'Volver a planificar', example: "The feature failed, so it's back to the drawing board." },
      { phrase: 'Beat around the bush', meaning: 'Andar con rodeos', example: "Stop beating around the bush and tell me the truth." }
    ]
  }
];

export const STUDY_MODES = ['flashcards', 'speaking', 'writing'] as const;