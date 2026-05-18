import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import type { ViewState, StudyMode } from './types';
import { pagesData } from './constants';

export const useVerbsStudy = () => {
  const navigate = useNavigate();
  const [view, setView] = useState<ViewState>('selection');
  const [selectedPages, setSelectedPages] = useState<string[]>([]);
  const [studyMode, setStudyMode] = useState<StudyMode>('flashcards');
  const [revealed, setRevealed] = useState(false);
  const [currentVerbIndex, setCurrentVerbIndex] = useState(0);

  const allVerbs = pagesData
    .filter(p => selectedPages.includes(p.id))
    .flatMap(p => p.verbs);
  
  const currentVerb = allVerbs[currentVerbIndex];
  const totalVerbs = allVerbs.length;

  const handleBack = () => {
    if (view === 'study') {
      setView('selection');
      setRevealed(false);
      setCurrentVerbIndex(0);
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
      setCurrentVerbIndex(0);
      setRevealed(false);
    }
  };

  const handleReveal = () => {
    setRevealed(true);
  };

  const handleNextVerb = () => {
    if (currentVerbIndex < totalVerbs - 1) {
      setCurrentVerbIndex(prev => prev + 1);
      setRevealed(false);
    } else {
      navigate('/dashboard');
    }
  };

  return {
    view,
    selectedPages,
    studyMode,
    revealed,
    currentVerbIndex,
    totalVerbs,
    currentVerb,
    handleBack,
    togglePageSelection,
    handleStartStudy,
    handleReveal,
    handleNextVerb,
    setStudyMode,
    pagesData,
  };
};