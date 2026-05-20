import { useNavigate } from 'react-router-dom';
import { 
  BookOpen, 
  CheckCircle2, 
  Play, 
  Volume2, 
  Mic, 
  PenTool, 
  Shuffle,
  X,
  Check,
  Home
} from 'lucide-react';
import { 
  Container,
  BackgroundGlow,
  MainContent,
  TopBar,
  BackButton,
  DashboardButton,
  HeaderTitle,
  Spacer,
  SelectionTitle,
  SelectionSubtitle,
  CardsGrid,
  PageCard,
  PageTitle,
  PageSubtitle,
  CheckIconWrapper,
  FloatingActionBar,
  ModeSelector,
  ModeButton,
  SelectionInfo,
  SelectionCountLabel,
  SelectionNumber,
  StartButton,
  CardContainer,
  SpeakerButton,
  MainWord,
  TapHint,
  ControlsContainer,
  ControlButton,
  PhaseBadge,
  ProgressInfo
} from '../../components/StudyShared';
import { useVocabularyStudy } from './hooks';
import { BOOK_PAGES, STUDY_MODES } from './constants';
import { TranslationText } from './styles';
import { WritingMode } from '../../components/WritingMode';

export const VocabularyStudy = () => {
  const navigate = useNavigate();
  const {
    view,
    selectedPages,
    studyMode,
    isFlipped,
    currentWordIndex,
    totalWords,
    currentWord,
    handleBack,
    togglePage,
    startStudySession,
    handleFlip,
    handleGotIt,
    handleReviewLater,
    handleWritingAnswer,
    setStudyMode,
  } = useVocabularyStudy();

  const renderStudyContent = () => {
    if (studyMode === 'writing') {
      return (
        <WritingMode
          word={currentWord.word}
          meaning={currentWord.translation}
          timeLimit={5}
          onAnswer={handleWritingAnswer}
          currentIndex={currentWordIndex}
          totalWords={totalWords}
        />
      );
    }

    return (
      <>
        <PhaseBadge>
          <BookOpen size={14} />
          Phase 1: Recognition
        </PhaseBadge>

        <CardContainer $revealed={isFlipped} onClick={!isFlipped ? handleFlip : undefined}>
          <SpeakerButton onClick={(e) => e.stopPropagation()}>
            <Volume2 size={22} />
          </SpeakerButton>
          
          <MainWord>{currentWord.word}</MainWord>
          
          {!isFlipped && (
            <TapHint>Tap to reveal translation</TapHint>
          )}
          
          {isFlipped && (
            <>
              <TranslationText>{currentWord.translation}</TranslationText>
              <TapHint style={{ fontStyle: 'italic' }}>"{currentWord.example}"</TapHint>
            </>
          )}
        </CardContainer>

        {isFlipped && (
          <ControlsContainer>
            <ControlButton 
              $variant="reject" 
              onClick={handleReviewLater}
            >
              <X size={28} />
            </ControlButton>
            <ControlButton 
              $variant="approve" 
              onClick={handleGotIt}
            >
              <Check size={28} />
            </ControlButton>
          </ControlsContainer>
        )}

        <ProgressInfo>
          {currentWordIndex + 1} / {totalWords} words
        </ProgressInfo>
      </>
    );
  };

  return (
    <Container>
      <BackgroundGlow />
      
      <TopBar>
        {view === 'study' ? (
          <BackButton onClick={handleBack}>
            <BookOpen size={18} />
            Back
          </BackButton>
        ) : (
          <DashboardButton onClick={() => navigate('/dashboard')}>
            <Home size={18} />
            Dashboard
          </DashboardButton>
        )}
        
        <HeaderTitle>
          <BookOpen size={20} />
          {view === 'selection' ? 'Set up your session' : `Mode: ${studyMode.toUpperCase()}`}
        </HeaderTitle>
        
        <Spacer />
      </TopBar>

      <MainContent>
        {view === 'selection' ? (
          <>
            <SelectionTitle>Select your pages</SelectionTitle>
            <SelectionSubtitle>Choose the pages to generate a practice session</SelectionSubtitle>
            
            <CardsGrid>
              {BOOK_PAGES.map((page) => (
                <PageCard 
                  key={page.num} 
                  $selected={selectedPages.includes(page.num)}
                  onClick={() => togglePage(page.num)}
                >
                  <CheckIconWrapper $selected={selectedPages.includes(page.num)}>
                    {selectedPages.includes(page.num) && <CheckCircle2 size={14} />}
                  </CheckIconWrapper>
                  <PageTitle>{page.title}</PageTitle>
                  <PageSubtitle>{page.desc}</PageSubtitle>
                </PageCard>
              ))}
            </CardsGrid>
          </>
        ) : (
          renderStudyContent()
        )}
      </MainContent>

      {view === 'selection' && selectedPages.length > 0 && (
        <FloatingActionBar $isVisible={selectedPages.length > 0}>
          <ModeSelector>
            {STUDY_MODES.map((mode) => (
              <ModeButton 
                key={mode}
                $active={studyMode === mode} 
                onClick={() => setStudyMode(mode)}
              >
                {mode === 'mixed' && <Shuffle size={16} />}
                {mode === 'speaking' && <Mic size={16} />}
                {mode === 'writing' && <PenTool size={16} />}
                {mode.charAt(0).toUpperCase() + mode.slice(1)}
              </ModeButton>
            ))}
          </ModeSelector>
          
          <SelectionInfo>
            <SelectionCountLabel>Pages Selected</SelectionCountLabel>
            <SelectionNumber>{selectedPages.length}</SelectionNumber>
          </SelectionInfo>
          
          <StartButton onClick={startStudySession}>
            <Play size={18} />
            Start Study
          </StartButton>
        </FloatingActionBar>
      )}
    </Container>
  );
};