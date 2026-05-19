import styled, { keyframes } from 'styled-components';

const flipIn = keyframes`
  from { opacity: 0; transform: rotateY(90deg); }
  to { opacity: 1; transform: rotateY(0); }
`;

export const FlipCardContainer = styled.div`
  perspective: 1000px;
  width: 100%;
  max-width: 450px;
  height: 280px;
  cursor: pointer;
  animation: ${flipIn} 0.6s ease-out;
`;

export const FlipCardInner = styled.div<{ $isFlipped: boolean }>`
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  transform: ${({ $isFlipped }) => $isFlipped ? 'rotateY(180deg)' : 'rotateY(0)'};
`;

export const FlipCardFace = styled.div`
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 24px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
`;

export const FlipCardFront = styled(FlipCardFace)``;

export const FlipCardBack = styled(FlipCardFace)`
  transform: rotateY(180deg);
  background: rgba(168, 85, 247, 0.08);
  border-color: rgba(168, 85, 247, 0.2);
`;

export const WordText = styled.h2`
  font-size: 3rem;
  font-weight: 700;
  color: white;
  text-align: center;
  margin: 0;
`;

export const TapHint = styled.p`
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
  margin-top: 1rem;
`;

export const SynonymText = styled.h2`
  font-size: 3rem;
  font-weight: 700;
  color: #a855f7;
  text-align: center;
  margin: 0;
`;