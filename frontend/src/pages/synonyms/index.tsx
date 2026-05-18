import { useNavigate } from 'react-router-dom';
import { 
  Layers,
  BookOpen,
  CheckCircle2, 
  Play, 
  Mic, 
  PenTool, 
  Shuffle,
  Volume2,
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
  SpeakerButton,
  ControlsContainer,
  ControlButton,
  PhaseBadge,
  ProgressInfo
} from '../../components/StudyShared';
import { useSynonymsStudy } from './hooks';
import { STUDY_MODES } from './constants';
import { FlipCardContainer, FlipCardInner, FlipCardFront, FlipCardBack, WordText, TapHint, SynonymText } from './styles';

export const SynonymsStudy = () => {
  const navigate = useNavigate();
  const {
    view, selectedPages, studyMode, isFlipped, currentIndex,
    totalItems, currentItem, handleBack, togglePageSelection,
    handleStartStudy, handleFlip, handleNext, setStudyMode, pagesData
  } = useSynonymsStudy();

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
          <Layers size={20} />
          {view === 'selection' ? 'Select your Synonym Pages' : `Mode: ${studyMode.toUpperCase()}`}
        </HeaderTitle>
        
        <Spacer />
      </TopBar>

      <MainContent>
        {view === 'selection' ? (
          <>
            <SelectionTitle>Select your Synonym Pages</SelectionTitle>
            <SelectionSubtitle>Choose the pages you want to study today</SelectionSubtitle>
            
            <CardsGrid>
              {pagesData.map((page) => (
                <PageCard
                  key={page.id}
                  $selected={selectedPages.includes(page.id)}
                  onClick={() => togglePageSelection(page.id)}
                >
                  <CheckIconWrapper $selected={selectedPages.includes(page.id)}>
                    {selectedPages.includes(page.id) && <CheckCircle2 size={14} />}
                  </CheckIconWrapper>
                  <PageTitle>Page {page.pageNumber}</PageTitle>
                  <PageSubtitle>{page.subtitle}</PageSubtitle>
                </PageCard>
              ))}
            </CardsGrid>
          </>
        ) : (
          <>
            <PhaseBadge>
              <Layers size={14} />
              Phase: Synonym Recall
            </PhaseBadge>

            <FlipCardContainer onClick={handleFlip}>
              <FlipCardInner $isFlipped={isFlipped}>
                <FlipCardFront>
                  <SpeakerButton onClick={(e) => e.stopPropagation()}>
                    <Volume2 size={22} />
                  </SpeakerButton>
                  <WordText>{currentItem?.word}</WordText>
                  <TapHint>Tap to flip</TapHint>
                </FlipCardFront>
                <FlipCardBack>
                  <SpeakerButton onClick={(e) => e.stopPropagation()}>
                    <Volume2 size={22} />
                  </SpeakerButton>
                  <SynonymText>{currentItem?.synonym}</SynonymText>
                  <TapHint>Tap to flip back</TapHint>
                </FlipCardBack>
              </FlipCardInner>
            </FlipCardContainer>

            {isFlipped && (
              <ControlsContainer>
                <ControlButton $variant="reject" onClick={handleNext}>
                  <X size={28} />
                </ControlButton>
                <ControlButton $variant="approve" onClick={handleNext}>
                  <Check size={28} />
                </ControlButton>
              </ControlsContainer>
            )}

            <ProgressInfo>
              {currentIndex + 1} / {totalItems} words
            </ProgressInfo>
          </>
        )}
      </MainContent>

      <FloatingActionBar $isVisible={view === 'selection' && selectedPages.length > 0}>
        <ModeSelector>
          {STUDY_MODES.map((mode) => (
            <ModeButton 
              key={mode}
              $active={studyMode === mode} 
              onClick={() => setStudyMode(mode)}
            >
              {mode === 'flashcards' && <Shuffle size={16} />}
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
        
        <StartButton onClick={handleStartStudy}>
          <Play size={18} />
          Start Study
        </StartButton>
      </FloatingActionBar>
    </Container>
  );
};