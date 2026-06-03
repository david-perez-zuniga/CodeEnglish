const BASE = import.meta.env.VITE_URL_BACKEND || 'http://localhost:8000';

export const API = {
  vocabulary: {
    byPage: (id: number) => `${BASE}/api/rt_vocabularies/vocabulary/${id}`,
  },
  pages: {
    byModule: (type: string) => `${BASE}/api/rt_pages/pages/${type}`,
  },
  idioms: {
    byPage: (id: number) => `${BASE}/api/rt_idioms/idiom/${id}`,
  },
};
