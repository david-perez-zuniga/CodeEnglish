import styled from 'styled-components';
import { fadeIn } from '../../components/StudyShared';

export const ConjugationsContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  width: 100%;
  margin-top: 2rem;
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  animation: ${fadeIn} 0.5s ease-out;

  @media (max-width: 500px) {
    grid-template-columns: 1fr;
  }
`;

export const ConjugationItem = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
`;

export const ConjugationLabel = styled.span`
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.5);
  text-transform: uppercase;
  letter-spacing: 0.05em;
`;

export const ConjugationValue = styled.span`
  font-size: 1.5rem;
  font-weight: 600;
  color: white;
  text-align: center;
`;

export const SpanishTranslation = styled.span`
  font-size: 1.1rem;
  color: #a855f7;
  text-align: center;
`;