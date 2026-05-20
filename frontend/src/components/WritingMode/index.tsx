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
  timeLimit,
  onAnswer,
  currentIndex,
  totalWords,
}: ExtendedWritingModeProps) => {
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
  } = useWritingMode(word, timeLimit, onAnswer);

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
            <FeedbackBannerAnswer>{word}</FeedbackBannerAnswer>
          )}
        </FeedbackBanner>
      )}

      {isTimeUp && !showFeedback && (
        <FeedbackBanner $isCorrect={false}>
          <Clock size={20} />
          <FeedbackBannerText $isCorrect={false}>Time's Up!</FeedbackBannerText>
          <FeedbackBannerAnswer>{word}</FeedbackBannerAnswer>
        </FeedbackBanner>
      )}

      <MeaningText>{meaning}</MeaningText>
      <InstructionText>Write the word in English</InstructionText>

      <WritingInput
        ref={inputRef}
        type="text"
        value={userInput}
        onChange={(e) => handleInputChange(e.target.value)}
        onFocus={handleInputFocus}
        onKeyDown={handleKeyDown}
        placeholder="Type your answer..."
        disabled={showFeedback}
      />

      <SubmitHint>Press ENTER to submit</SubmitHint>

      <ProgressInfo>
        {currentIndex + 1} / {totalWords} words
      </ProgressInfo>
    </WritingContainer>
  );
};