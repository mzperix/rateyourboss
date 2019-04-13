'use strict';
function _defineProperty(obj, key, value) {if (key in obj) {Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true });} else {obj[key] = value;}return obj;}
const boses = [
{
  name: 'Elon Musk',
  year: 1972 },

{
  name: 'Elon Musk Junior',
  year: 2000 },

{
  name: 'Eishay Smith',
  year: 1983 },

{
  name: 'Elon Musk Junior',
  year: 2007 },];


// https://developer.mozilla.org/en/docs/Web/JavaScript/Guide/Regular_Expressions#Using_Special_Characters
function escapeRegexCharacters(str) {
  return str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function getSuggestions(value) {
  const escapedValue = escapeRegexCharacters(value.trim());

  if (escapedValue === '') {
    return [];
  }

  const regex = new RegExp('^' + escapedValue, 'i');

  return bosses.filter(boss => regex.test(boss.name));
}

function getSuggestionValue(suggestion) {
  return suggestion.name;
}

function renderSuggestion(suggestion, { query }) {
  const matches = AutosuggestHighlightMatch(suggestion.name, query);
  const parts = AutosuggestHighlightParse(suggestion.name, matches);

  return (
    React.createElement("span", null,
    parts.map((part, index) => {
      const className = part.highlight ? 'react-autosuggest__suggestion-match' : null;

      return (
        React.createElement("span", { className: className, key: index },
        part.text));


    })));


}

class App extends React.Component {
  constructor() {
    super();_defineProperty(this, "onChange",



    (event, { newValue, method }) => {
      this.setState({
        value: newValue });

    });_defineProperty(this, "onSuggestionsFetchRequested",

    ({ value }) => {
      this.setState({
        suggestions: getSuggestions(value) });

    });_defineProperty(this, "onSuggestionsClearRequested",

    () => {
      this.setState({
        suggestions: [] });

    });this.state = { value: '', suggestions: [] };}

  render() {
    const { value, suggestions } = this.state;
    const inputProps = {
      placeholder: "Enter your boss's name",
      value,
      onChange: this.onChange };


    return (
      React.createElement(Autosuggest, {
        suggestions: suggestions,
        onSuggestionsFetchRequested: this.onSuggestionsFetchRequested,
        onSuggestionsClearRequested: this.onSuggestionsClearRequested,
        getSuggestionValue: getSuggestionValue,
        renderSuggestion: renderSuggestion,
        inputProps: inputProps }));


  }}


ReactDOM.render(React.createElement(App, null), document.getElementById('app'));