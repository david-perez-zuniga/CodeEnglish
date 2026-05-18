import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import type { ViewState, StudyMode } from './types';
import { pagesData } from './constants';

export const useSynonymsStudy = () => {
  const navigate = useNavigate();
  const [view, setView] = useState<ViewState>('selection');
  const [selectedPages, setSelectedPages] = useState<string[]>([]);
  const [studyMode, setStudyMode] = useState<StudyMode>('flashcards');
  const [isFlipped, setIsFlipped] = useState(false);
  const [currentIndex, setCurrentIndex] = useState(0);

  const allItems = pagesData
    .filter(p => selectedPages.includes(p.id))
    .flatMap(p => p.synonyms);
  
  const currentItem = allItems[currentIndex];
  const totalItems = allItems.length;

  const handleBack = () => {
    if (view === 'study') {
      setView('selection');
      setIsFlipped(false);
      setCurrentIndex(0);
    } else {
      navigate('/dashboard');
    }
  };

  const togglePageSelection = (pageId: string) => {
    setSelectedPages(prev => 
      prev.includes(pageId) ? prev.filter(id => id !== pageId) : [...prev, pageId]
    );
  };

  const handleStartStudy = () => {
    if (selectedPages.length > 0) {
      setView('study');
      setCurrentIndex(0);
      setIsFlipped(false);
    }
  };

  const handleFlip = () => setIsFlipped(!isFlipped);

  const handleNext = () => {
    if (currentIndex < totalItems - 1) {
      setCurrentIndex(prev => prev + 1);
      setIsFlipped(false);
    } else {
      navigate('/dashboard');
    }
  };

  return {
    view, selectedPages, studyMode, isFlipped, currentIndex,
    totalItems, currentItem, handleBack, togglePageSelection,
    handleStartStudy, handleFlip, handleNext, setStudyMode, pagesData
  };
};