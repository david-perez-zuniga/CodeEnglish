import { useNavigate } from 'react-router-dom';
import { 
  Quote,
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
  CardContainer,
  SpeakerButton,
  MainWord,
  TapHint,
  ControlsContainer,
  ControlButton,
  PhaseBadge,
  ProgressInfo
} from '../../components/StudyShared';
import { useSayingsStudy } from './hooks';
import { STUDY_MODES } from './constants';
import { MeaningText, ExampleContainer, ExampleLabel, ExampleText } from './styles';

export const SayingsStudy = () => {
  const navigate = useNavigate();
  const {
    view, selectedPages, studyMode, revealed, currentIndex,
    totalItems, currentItem, handleBack, togglePageSelection,
    handleStartStudy, handleReveal, handleNext, setStudyMode, pagesData
  } = useSayingsStudy();

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
          <Quote size={20} />
          {view === 'selection' ? 'Select your Saying Pages' : `Mode: ${studyMode.toUpperCase()}`}
        </HeaderTitle>
        
        <Spacer />
      </TopBar>

      <MainContent>
        {view === 'selection' ? (
          <>
            <SelectionTitle>Select your Saying Pages</SelectionTitle>
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
              <Quote size={14} />
              Phase: Saying Reveal
            </PhaseBadge>

            <CardContainer $revealed={revealed} onClick={!revealed ? handleReveal : undefined}>
              <SpeakerButton onClick={(e) => e.stopPropagation()}>
                <Volume2 size={22} />
              </SpeakerButton>
              
              <MainWord>{currentItem?.saying}</MainWord>
              
              {!revealed && (
                <TapHint>Tap to reveal meaning</TapHint>
              )}
              
              {revealed && currentItem && (
                <>
                  <MeaningText>{currentItem.meaning}</MeaningText>
                  <ExampleContainer>
                    <ExampleLabel>Example</ExampleLabel>
                    <ExampleText>"{currentItem.example}"</ExampleText>
                  </ExampleContainer>
                </>
              )}
            </CardContainer>

            {revealed && (
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
              {currentIndex + 1} / {totalItems} sayings
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