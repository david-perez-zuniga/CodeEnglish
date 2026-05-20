export const isCorrectAnswer = (userInput: string, correctAnswer: string): boolean => {
  return userInput.toLowerCase().trim() === correctAnswer.toLowerCase().trim();
};