import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Welcome } from './pages/Welcome';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { Dashboard } from './pages/Dashboard';
import { VocabularyStudy } from './pages/vocabulary';
import { VerbsStudy } from './pages/verbs';
import { IdiomsStudy } from './pages/idioms';
import { SynonymsStudy } from './pages/synonyms';
import { SayingsStudy } from './pages/sayings';
import { CountriesStudy } from './pages/countries';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/dashboard/vocabulary" element={<VocabularyStudy />} />
        <Route path="/dashboard/verbs" element={<VerbsStudy />} />
        <Route path="/dashboard/idioms" element={<IdiomsStudy />} />
        <Route path="/dashboard/synonyms" element={<SynonymsStudy />} />
        <Route path="/dashboard/sayings" element={<SayingsStudy />} />
        <Route path="/dashboard/countries" element={<CountriesStudy />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
