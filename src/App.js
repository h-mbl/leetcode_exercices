import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import { useTranslation } from 'react-i18next';

// ... Autres composants (Header, ProblemCard, ProblemList) restent inchangés ...

// Mise à jour du composant ProblemDetail pour utiliser useParams
import { useParams } from 'react-router-dom';
import * as PropTypes from "prop-types";

const ProblemDetail = () => {
  const { t } = useTranslation();
  const { id } = useParams();

  // Ici, vous devriez récupérer les détails du problème en utilisant l'id
  const problem = dummyProblem; // À remplacer par la logique de récupération réelle

  return (
    <div className="problem-detail">
      <h2>{problem.title}</h2>
      <p>{t('link')}: <a href={problem.leetCodeLink} target="_blank" rel="noopener noreferrer">{t('leetCodeProblem')}</a></p>
      <h3>{t('pythonSolution')}</h3>
      <pre><code>{problem.pythonSolution}</code></pre>
      <h3>{t('cppSolution')}</h3>
      <pre><code>{problem.cppSolution}</code></pre>
      <img src={problem.screenshot} alt={t('problemScreenshot')} />
    </div>
  );
};

// Données factices
const dummyProblems = [
  { id: 1, title: 'Two Sum', difficulty: 'Easy', timeComplexity: 'O(n)', spaceComplexity: 'O(n)' },
  { id: 2, title: 'Add Two Numbers', difficulty: 'Medium', timeComplexity: 'O(max(m,n))', spaceComplexity: 'O(max(m,n))' },
];

const dummyProblem = {
  id: 1,
  title: 'Two Sum',
  difficulty: 'Easy',
  timeComplexity: 'O(n)',
  spaceComplexity: 'O(n)',
  leetCodeLink: 'https://leetcode.com/problems/two-sum/',
  pythonSolution: 'def twoSum(self, nums, target):\n    # Solution code here',
  cppSolution: 'vector<int> twoSum(vector<int>& nums, int target) {\n    // Solution code here\n}',
  screenshot: 'https://example.com/two-sum-screenshot.png'
};

function Header() {
  return null;
}

function ProblemList(props) {
  return null;
}

ProblemList.propTypes = {problems: PropTypes.any};
const App = () => {
  const { t } = useTranslation();

  return (
    <Router>
      <div className="app">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<h2>{t('welcome')}</h2>} />
            <Route path="/problems" element={<ProblemList problems={dummyProblems} />} />
            <Route path="/problem/:id" element={<ProblemDetail />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;