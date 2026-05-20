import styled, { keyframes, css } from 'styled-components';

const fadeIn = keyframes`
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
`;

const pulse = keyframes`
  0% { transform: scale(1); }
  50% { transform: scale(1.05); }
  100% { transform: scale(1); }
`;

export const WritingContainer = styled.div`
  width: 100%;
  max-width: 600px;
  padding: 2rem;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: ${fadeIn} 0.6s ease-out;
  position: relative;
`;

export const TimerContainer = styled.div`
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  margin-bottom: 1rem;
  overflow: hidden;
`;

export const TimerBar = styled.div<{ $percentage: number; $isWarning: boolean }>`
  height: 100%;
  width: ${({ $percentage }) => $percentage}%;
  background: ${({ $isWarning }) => 
    $isWarning 
      ? 'linear-gradient(90deg, #ef4444, #f97316)' 
      : 'linear-gradient(90deg, #6366f1, #a855f7)'
  };
  border-radius: 3px;
  transition: width 0.1s linear, background 0.3s ease;
`;

export const FeedbackBanner = styled.div<{ $isCorrect: boolean }>`
  width: 100%;
  padding: 0.75rem 1rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  animation: ${fadeIn} 0.3s ease-out;

  ${({ $isCorrect }) => $isCorrect ? css`
    background: rgba(34, 197, 94, 0.15);
    border: 1px solid rgba(34, 197, 94, 0.3);
  ` : css`
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid rgba(239, 68, 68, 0.3);
  `}
`;

export const FeedbackBannerText = styled.span<{ $isCorrect: boolean }>`
  font-size: 1rem;
  font-weight: 600;
  color: ${({ $isCorrect }) => $isCorrect ? '#22c55e' : '#ef4444'};
`;

export const FeedbackBannerAnswer = styled.span`
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.8);
  font-weight: 500;
`;

export const MeaningText = styled.h2`
  font-size: 2.5rem;
  font-weight: 700;
  color: #a855f7;
  margin-bottom: 0.5rem;
  text-align: center;
`;

export const InstructionText = styled.p`
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.6);
  margin-bottom: 1.5rem;
  text-align: center;
`;

export const WritingInput = styled.input`
  width: 100%;
  max-width: 400px;
  padding: 1rem 1.5rem;
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.05);
  border: 2px solid rgba(99, 102, 241, 0.3);
  color: white;
  font-size: 1.5rem;
  font-weight: 600;
  text-align: center;
  outline: none;
  transition: all 0.3s ease;

  &::placeholder {
    color: rgba(255, 255, 255, 0.3);
    font-weight: 400;
  }

  &:focus {
    border-color: #6366f1;
    background: rgba(99, 102, 241, 0.1);
    box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
  }
`;

export const SubmitHint = styled.p`
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.4);
  margin-top: 1rem;
`;

export const FeedbackOverlay = styled.div<{ $isCorrect: boolean }>`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  animation: ${fadeIn} 0.3s ease-out;
  z-index: 10;

  ${({ $isCorrect }) => $isCorrect ? css`
    background: rgba(34, 197, 94, 0.15);
    border: 2px solid rgba(34, 197, 94, 0.4);
  ` : css`
    background: rgba(239, 68, 68, 0.15);
    border: 2px solid rgba(239, 68, 68, 0.4);
  `}
`;

export const FeedbackIcon = styled.div<{ $isCorrect: boolean }>`
  width: 80px;
  height: 80px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
  animation: ${pulse} 0.5s ease-out;

  ${({ $isCorrect }) => $isCorrect ? css`
    background: rgba(34, 197, 94, 0.2);
    color: #22c55e;
  ` : css`
    background: rgba(239, 68, 68, 0.2);
    color: #ef4444;
  `}
`;

export const FeedbackText = styled.span<{ $isCorrect: boolean }>`
  font-size: 1.5rem;
  font-weight: 700;
  color: ${({ $isCorrect }) => $isCorrect ? '#22c55e' : '#ef4444'};
`;

export const CorrectAnswer = styled.div`
  margin-top: 0.5rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.1);
`;

export const CorrectAnswerLabel = styled.span`
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.6);
`;

export const CorrectAnswerWord = styled.span`
  font-size: 1.1rem;
  font-weight: 700;
  color: white;
  margin-left: 0.5rem;
`;

export const TimeUpOverlay = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 24px;
  background: rgba(239, 68, 68, 0.15);
  border: 2px solid rgba(239, 68, 68, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  animation: ${fadeIn} 0.3s ease-out;
  z-index: 10;
`;

export const TimeUpText = styled.span`
  font-size: 1.5rem;
  font-weight: 700;
  color: #ef4444;
`;

export const TimeUpAnswer = styled.div`
  margin-top: 1rem;
  text-align: center;
`;

export const ProgressInfo = styled.div`
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1.5rem;
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
`;