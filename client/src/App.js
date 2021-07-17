import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Home from './views/Home';
import About from './views/About';

import Header from './components/Header';
import Footer from './components/Footer';


function App() {
  return (
    <Router>
      <Header></Header>
      <Switch>
        <Route path='/about' component={ About }></Route>
        <Route path='/' component={ Home }></Route>
      </Switch>
      <Footer></Footer>
    </Router>
  );
}

export default App;
