import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import type { ViewState, StudyMode, Word } from './types';
import { mockWords } from './constants';

const API_BASE = 'http://localhost:8000/api/rt_vocabularies';

export const useVocabularyStudy = () => {
  const navigate = useNavigate();
  const [view, setView] = useState<ViewState>('selection');
  const [selectedPages, setSelectedPages] = useState<number[]>([]);
  const [studyMode, setStudyMode] = useState<StudyMode>('mixed');
  const [isFlipped, setIsFlipped] = useState(false);
  const [currentWordIndex, setCurrentWordIndex] = useState(0);
  const [words, setWords] = useState<Word[]>(mockWords);
  const [loading, setLoading] = useState(false);
  const [currentWordMode, setCurrentWordMode] = useState<'english' | 'spanish'>('english');

  const fetchVocabularyByPages = async (pages: number[]) => {
    setLoading(true);
    try {
      const allWords: Word[] = [];
      for (const pageNum of pages) {
        const response = await fetch(`${API_BASE}/vocabulary/${pageNum}`);
        if (response.ok) {
          const data = await response.json();
          const mapped = data.map((item: any) => ({
            id: item.id,
            word: item.word,
            translation: item.meaning,
            example: ''
          }));
          allWords.push(...mapped);
        }
      }
      if (allWords.length > 0) {
        setWords(allWords.slice(0, 15));
      }
    } catch (error) {
      console.error('Error fetching vocabulary:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (selectedPages.length > 0) {
      fetchVocabularyByPages(selectedPages);
    }
  }, [selectedPages]);

  const currentWord = words[currentWordIndex];
  const totalWords = words.length;

  const handleBack = () => {
    if (view === 'study') {
      setView('selection');
      setIsFlipped(false);
      setCurrentWordIndex(0);
    } else {
      navigate('/dashboard');
    }
  };

  const togglePage = (pageNum: number) => {
    setSelectedPages((prev) => 
      prev.includes(pageNum) ? prev.filter(p => p !== pageNum) : [...prev, pageNum]
    );
  };

  const startStudySession = () => {
    setView('study');
    setCurrentWordIndex(0);
    setIsFlipped(false);
    setCurrentWordMode(Math.random() < 0.5 ? 'english' : 'spanish');
  };

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const handleNextWord = () => {
    if (currentWordIndex < totalWords - 1) {
      setCurrentWordIndex(prev => prev + 1);
      setIsFlipped(false);
      setCurrentWordMode(Math.random() < 0.5 ? 'english' : 'spanish');
    } else {
      navigate('/dashboard');
    }
  };

  const handleGotIt = () => handleNextWord();
  const handleReviewLater = () => handleNextWord();

  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const handleWritingAnswer = (_isCorrect: boolean, _isEnglish: boolean) => {
    setTimeout(() => {
      handleNextWord();
    }, 1500);
  };

  return {
    view,
    selectedPages,
    studyMode,
    isFlipped,
    currentWordIndex,
    totalWords,
    currentWord,
    currentWordMode,
    handleBack,
    togglePage,
    startStudySession,
    handleFlip,
    handleNextWord,
    handleGotIt,
    handleReviewLater,
    handleWritingAnswer,
    setStudyMode,
    loading,
  };
};