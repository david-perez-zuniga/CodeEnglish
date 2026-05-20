import { useState, useEffect, useCallback, useRef } from 'react';
import { isCorrectAnswer } from '../../utils/stringValidator';

export const useWritingMode = (
  correctWord: string,
  answer: string,
  timeLimit: number,
  onAnswer: (isCorrect: boolean, isEnglish: boolean) => void
) => {
  const [userInput, setUserInput] = useState('');
  const [timeLeft, setTimeLeft] = useState(timeLimit);
  const [isActive, setIsActive] = useState(false);
  const [isTimeUp, setIsTimeUp] = useState(false);
  const [showFeedback, setShowFeedback] = useState(false);
  const [isCorrect, setIsCorrect] = useState<boolean | null>(null);
  
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const feedbackTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  const clearTimers = useCallback(() => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
    if (feedbackTimerRef.current) {
      clearTimeout(feedbackTimerRef.current);
      feedbackTimerRef.current = null;
    }
  }, []);

  useEffect(() => {
    return () => clearTimers();
  }, [clearTimers]);

  useEffect(() => {
    if (isActive && !isTimeUp && !showFeedback) {
      timerRef.current = setInterval(() => {
        setTimeLeft((prev) => {
          if (prev <= 0.1) {
            clearTimers();
            setIsTimeUp(true);
            setIsCorrect(false);
            setShowFeedback(true);
            onAnswer(false, answer === correctWord);

            feedbackTimerRef.current = setTimeout(() => {
              setShowFeedback(false);
              setUserInput('');
              setTimeLeft(timeLimit);
              setIsActive(false);
              setIsTimeUp(false);
              setIsCorrect(null);
            }, 1500);

            return 0;
          }
          return prev - 0.1;
        });
      }, 100);
    }

    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
      }
    };
  }, [isActive, isTimeUp, showFeedback, timeLimit, answer, correctWord, onAnswer, clearTimers]);

  const handleInputFocus = useCallback(() => {
    if (!isActive && !isTimeUp && !showFeedback) {
      setIsActive(true);
    }
  }, [isActive, isTimeUp, showFeedback]);

  const handleInputChange = useCallback((value: string) => {
    setUserInput(value);
  }, []);

  const handleSubmit = useCallback(() => {
    if (showFeedback || isTimeUp) return;

    clearTimers();
    const correct = isCorrectAnswer(userInput, answer);
    setIsCorrect(correct);
    setShowFeedback(true);
    onAnswer(correct, answer === correctWord);

    feedbackTimerRef.current = setTimeout(() => {
      setShowFeedback(false);
      setUserInput('');
      setTimeLeft(timeLimit);
      setIsActive(false);
      setIsTimeUp(false);
      setIsCorrect(null);
    }, 1500);
  }, [userInput, answer, correctWord, showFeedback, isTimeUp, timeLimit, onAnswer, clearTimers]);

  const handleKeyDown = useCallback((e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      handleSubmit();
    }
  }, [handleSubmit]);

  const percentage = (timeLeft / timeLimit) * 100;
  const isWarning = percentage < 30;

  return {
    userInput,
    timeLeft,
    percentage,
    isWarning,
    isActive,
    isTimeUp,
    showFeedback,
    isCorrect,
    handleInputFocus,
    handleInputChange,
    handleSubmit,
    handleKeyDown,
  };
};