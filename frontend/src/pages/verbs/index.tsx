import { useNavigate } from 'react-router-dom';
import { 
  Zap, 
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
import { useVerbsStudy } from './hooks';
import { STUDY_MODES } from './constants';
import { 
  ConjugationsContainer,
  ConjugationItem,
  ConjugationLabel,
  ConjugationValue,
  SpanishTranslation
} from './styles';

export const VerbsStudy = () => {
  const navigate = useNavigate();
  const {
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
  } = useVerbsStudy();

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
          <Zap size={20} />
          {view === 'selection' ? 'Select your Verb Pages' : `Mode: ${studyMode.toUpperCase()}`}
        </HeaderTitle>
        
        <Spacer />
      </TopBar>

      <MainContent>
        {view === 'selection' ? (
          <>
            <SelectionTitle>Select your Verb Pages</SelectionTitle>
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
                  <PageSubtitle $isIrregular={page.isIrregular}>{page.subtitle}</PageSubtitle>
                </PageCard>
              ))}
            </CardsGrid>
          </>
        ) : (
          <>
            <PhaseBadge>
              <Zap size={14} />
              Phase: Conjugation Reveal
            </PhaseBadge>

            <CardContainer $revealed={revealed} onClick={!revealed ? handleReveal : undefined}>
              <SpeakerButton onClick={(e) => e.stopPropagation()}>
                <Volume2 size={22} />
              </SpeakerButton>
              
              <MainWord>{currentVerb?.base}</MainWord>
              
              {!revealed && (
                <TapHint>Tap to reveal conjugations</TapHint>
              )}
              
              {revealed && currentVerb && (
                <ConjugationsContainer>
                  <ConjugationItem>
                    <ConjugationLabel>Past Simple</ConjugationLabel>
                    <ConjugationValue>{currentVerb.pastSimple}</ConjugationValue>
                  </ConjugationItem>
                  <ConjugationItem>
                    <ConjugationLabel>Past Participle</ConjugationLabel>
                    <ConjugationValue>{currentVerb.pastParticiple}</ConjugationValue>
                  </ConjugationItem>
                  <ConjugationItem>
                    <ConjugationLabel>Spanish</ConjugationLabel>
                    <SpanishTranslation>{currentVerb.spanish}</SpanishTranslation>
                  </ConjugationItem>
                </ConjugationsContainer>
              )}
            </CardContainer>

            {revealed && (
              <ControlsContainer>
                <ControlButton $variant="reject" onClick={handleNextVerb}>
                  <X size={28} />
                </ControlButton>
                <ControlButton $variant="approve" onClick={handleNextVerb}>
                  <Check size={28} />
                </ControlButton>
              </ControlsContainer>
            )}

            <ProgressInfo>
              {currentVerbIndex + 1} / {totalVerbs} verbs
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