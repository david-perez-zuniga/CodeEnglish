import { useEffect, useRef } from 'react';
import { Check, X, Clock } from 'lucide-react';
import type { WritingModeProps } from './types';
import { useWritingMode } from './hooks';
import {
  WritingContainer,
  TimerContainer,
  TimerBar,
  FeedbackBanner,
  FeedbackBannerText,
  FeedbackBannerAnswer,
  MeaningText,
  InstructionText,
  WritingInput,
  SubmitHint,
  ProgressInfo,
} from './styles';

interface ExtendedWritingModeProps extends WritingModeProps {
  currentIndex: number;
  totalWords: number;
}

export const WritingMode = ({
  word,
  meaning,
  answer,
  timeLimit,
  onAnswer,
  currentIndex,
  totalWords,
}: ExtendedWritingModeProps) => {
  const isEnglishMode = answer === word;
  const inputRef = useRef<HTMLInputElement>(null);

  const {
    userInput,
    percentage,
    isWarning,
    isActive,
    isTimeUp,
    showFeedback,
    isCorrect,
    handleInputFocus,
    handleInputChange,
    handleKeyDown,
  } = useWritingMode(word, answer, timeLimit, onAnswer);

  useEffect(() => {
    if (!showFeedback && inputRef.current) {
      setTimeout(() => inputRef.current?.focus(), 50);
    }
  }, [currentIndex, showFeedback]);

  return (
    <WritingContainer>
      <TimerContainer>
        <TimerBar $percentage={isActive ? percentage : 100} $isWarning={isActive && isWarning} />
      </TimerContainer>

      {showFeedback && isCorrect !== null && (
        <FeedbackBanner $isCorrect={isCorrect as boolean}>
          {isCorrect ? <Check size={20} /> : <X size={20} />}
          <FeedbackBannerText $isCorrect={isCorrect as boolean}>
            {isCorrect ? 'Correct!' : 'Incorrect'}
          </FeedbackBannerText>
{!isCorrect && (
            <FeedbackBannerAnswer>{answer}</FeedbackBannerAnswer>
          )}
        </FeedbackBanner>
      )}

      {isTimeUp && !showFeedback && (
        <FeedbackBanner $isCorrect={false}>
          <Clock size={20} />
          <FeedbackBannerText $isCorrect={false}>Time's Up!</FeedbackBannerText>
          <FeedbackBannerAnswer>{answer}</FeedbackBannerAnswer>
        </FeedbackBanner>
      )}

      <MeaningText>{isEnglishMode ? meaning : word}</MeaningText>
      <InstructionText>{isEnglishMode ? 'Write the word in English' : 'Escribe la palabra en español'}</InstructionText>

      <WritingInput
        ref={inputRef}
        type="text"
        value={userInput}
        onChange={(e) => handleInputChange(e.target.value)}
        onFocus={handleInputFocus}
        onKeyDown={handleKeyDown}
        placeholder={isEnglishMode ? 'Type your answer...' : 'Escribe tu respuesta...'}
        disabled={showFeedback}
      />

      <SubmitHint>{isEnglishMode ? 'Press ENTER to submit' : 'Presiona ENTER para enviar'}</SubmitHint>

      <ProgressInfo>
        {currentIndex + 1} / {totalWords} words
      </ProgressInfo>
    </WritingContainer>
  );
};