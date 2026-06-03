import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import type { ViewState, StudyMode, IdiomPage, IdiomData } from './types';
import { API } from '../../utils/api';

export const useIdiomsStudy = () => {
  const navigate = useNavigate();
  const [view, setView] = useState<ViewState>('selection');
  const [selectedPages, setSelectedPages] = useState<number[]>([]);
  const [studyMode, setStudyMode] = useState<StudyMode>('flashcards');
  const [revealed, setRevealed] = useState(false);
  const [currentIdiomIndex, setCurrentIdiomIndex] = useState(0);
  const [pagesData, setPagesData] = useState<IdiomPage[]>([]);
  const [allIdioms, setAllIdioms] = useState<IdiomData[]>([]);
  const [loading, setLoading] = useState(false);
  const [currentIdiomMode, setCurrentIdiomMode] = useState<'english' | 'spanish'>('english');

  useEffect(() => {
    const fetchPages = async () => {
      try {
        const response = await fetch(API.pages.byModule('idioms'));
        if (response.ok) {
          const data = await response.json();
          setPagesData(
            data.map((page: any) => ({
              id: page.id,
              pageNumber: page.page_number,
              subtitle: page.subtitle,
            }))
          );
        }
      } catch (error) {
        console.error('Error fetching idiom pages:', error);
      }
    };
    fetchPages();
  }, []);

  const currentIdiom = allIdioms[currentIdiomIndex];
  const totalIdioms = allIdioms.length;

  const writingAnswer = currentIdiomMode === 'english'
    ? currentIdiom?.phrase ?? ''
    : currentIdiom?.meaning ?? '';

  const handleBack = () => {
    if (view === 'study') {
      setView('selection');
      setRevealed(false);
      setCurrentIdiomIndex(0);
      setAllIdioms([]);
    } else {
      navigate('/dashboard');
    }
  };

  const togglePageSelection = (pageId: number) => {
    setSelectedPages(prev =>
      prev.includes(pageId)
        ? prev.filter(id => id !== pageId)
        : [...prev, pageId]
    );
  };

  const handleStartStudy = async () => {
    if (selectedPages.length === 0) return;

    setLoading(true);
    try {
      const idioms: IdiomData[] = [];
      for (const pageId of selectedPages) {
        const response = await fetch(API.idioms.byPage(pageId));
        if (response.ok) {
          const data = await response.json();
          idioms.push(
            ...data.map((item: any) => ({
              phrase: item.phrase,
              meaning: item.meaning,
              example: item.example,
            }))
          );
        }
      }
      setAllIdioms(idioms);
      setView('study');
      setCurrentIdiomIndex(0);
      setRevealed(false);
      setCurrentIdiomMode(Math.random() < 0.5 ? 'english' : 'spanish');
    } catch (error) {
      console.error('Error fetching idioms:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleReveal = () => setRevealed(true);

  const handleNextIdiom = () => {
    if (currentIdiomIndex < totalIdioms - 1) {
      setCurrentIdiomIndex(prev => prev + 1);
      setRevealed(false);
      setCurrentIdiomMode(Math.random() < 0.5 ? 'english' : 'spanish');
    } else {
      navigate('/dashboard');
    }
  };

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const handleWritingAnswer = (_isCorrect: boolean, _isEnglish: boolean) => {
    setTimeout(() => {
      handleNextIdiom();
    }, 1500);
  };

  return {
    view,
    selectedPages,
    studyMode,
    revealed,
    currentIdiomIndex,
    totalIdioms,
    currentIdiom,
    currentIdiomMode,
    writingAnswer,
    handleBack,
    togglePageSelection,
    handleStartStudy,
    handleReveal,
    handleNextIdiom,
    handleWritingAnswer,
    setStudyMode,
    pagesData,
    loading,
  };
};
