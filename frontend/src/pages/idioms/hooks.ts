import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import type { ViewState, StudyMode } from './types';
import { pagesData } from './constants';

export const useIdiomsStudy = () => {
  const navigate = useNavigate();
  const [view, setView] = useState<ViewState>('selection');
  const [selectedPages, setSelectedPages] = useState<string[]>([]);
  const [studyMode, setStudyMode] = useState<StudyMode>('flashcards');
  const [revealed, setRevealed] = useState(false);
  const [currentIdiomIndex, setCurrentIdiomIndex] = useState(0);

  const allIdioms = pagesData
    .filter(p => selectedPages.includes(p.id))
    .flatMap(p => p.idioms);
  
  const currentIdiom = allIdioms[currentIdiomIndex];
  const totalIdioms = allIdioms.length;

  const handleBack = () => {
    if (view === 'study') {
      setView('selection');
      setRevealed(false);
      setCurrentIdiomIndex(0);
    } else {
      navigate('/dashboard');
    }
  };

  const togglePageSelection = (pageId: string) => {
    setSelectedPages(prev => 
      prev.includes(pageId) 
        ? prev.filter(id => id !== pageId)
        : [...prev, pageId]
    );
  };

  const handleStartStudy = () => {
    if (selectedPages.length > 0) {
      setView('study');
      setCurrentIdiomIndex(0);
      setRevealed(false);
    }
  };

  const handleReveal = () => setRevealed(true);

  const handleNextIdiom = () => {
    if (currentIdiomIndex < totalIdioms - 1) {
      setCurrentIdiomIndex(prev => prev + 1);
      setRevealed(false);
    } else {
      navigate('/dashboard');
    }
  };

  return {
    view, selectedPages, studyMode, revealed, currentIdiomIndex,
    totalIdioms, currentIdiom, handleBack, togglePageSelection,
    handleStartStudy, handleReveal, handleNextIdiom, setStudyMode, pagesData
  };
};