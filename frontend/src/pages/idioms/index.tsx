import { useNavigate } from 'react-router-dom';
import { 
  MessageCircle,
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
import { useIdiomsStudy } from './hooks';
import { STUDY_MODES } from './constants';
import { MeaningText, ExampleContainer, ExampleLabel, ExampleText } from './styles';

export const IdiomsStudy = () => {
  const navigate = useNavigate();
  const {
    view, selectedPages, studyMode, revealed, currentIdiomIndex,
    totalIdioms, currentIdiom, handleBack, togglePageSelection,
    handleStartStudy, handleReveal, handleNextIdiom, setStudyMode, pagesData
  } = useIdiomsStudy();

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
          <MessageCircle size={20} />
          {view === 'selection' ? 'Select your Idiom Pages' : `Mode: ${studyMode.toUpperCase()}`}
        </HeaderTitle>
        
        <Spacer />
      </TopBar>

      <MainContent>
        {view === 'selection' ? (
          <>
            <SelectionTitle>Select your Idiom Pages</SelectionTitle>
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
              <MessageCircle size={14} />
              Phase: Idiom Reveal
            </PhaseBadge>

            <CardContainer $revealed={revealed} onClick={!revealed ? handleReveal : undefined}>
              <SpeakerButton onClick={(e) => e.stopPropagation()}>
                <Volume2 size={22} />
              </SpeakerButton>
              
              <MainWord>{currentIdiom?.phrase}</MainWord>
              
              {!revealed && (
                <TapHint>Tap to reveal meaning</TapHint>
              )}
              
              {revealed && currentIdiom && (
                <>
                  <MeaningText>{currentIdiom.meaning}</MeaningText>
                  <ExampleContainer>
                    <ExampleLabel>Example</ExampleLabel>
                    <ExampleText>"{currentIdiom.example}"</ExampleText>
                  </ExampleContainer>
                </>
              )}
            </CardContainer>

            {revealed && (
              <ControlsContainer>
                <ControlButton $variant="reject" onClick={handleNextIdiom}>
                  <X size={28} />
                </ControlButton>
                <ControlButton $variant="approve" onClick={handleNextIdiom}>
                  <Check size={28} />
                </ControlButton>
              </ControlsContainer>
            )}

            <ProgressInfo>
              {currentIdiomIndex + 1} / {totalIdioms} idioms
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