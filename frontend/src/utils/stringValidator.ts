const normalizeAccents = (str: string): string => {
  return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
};

export const isCorrectAnswer = (userInput: string, correctAnswer: string): boolean => {
  const normalizedUser = normalizeAccents(userInput.toLowerCase().trim());
  const normalizedCorrect = normalizeAccents(correctAnswer.toLowerCase().trim());
  return normalizedUser === normalizedCorrect;
};