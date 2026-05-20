export interface WritingState {
  userInput: string;
  isCorrect: boolean | null;
  isTimeUp: boolean;
  showFeedback: boolean;
}

export interface WritingModeProps {
  word: string;
  meaning: string;
  timeLimit: number;
  onAnswer: (isCorrect: boolean) => void;
}

export type AnswerResult = 'correct' | 'incorrect' | 'timeout';