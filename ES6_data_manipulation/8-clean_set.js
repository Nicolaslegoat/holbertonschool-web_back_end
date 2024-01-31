/* eslint-disable */
export default function cleanSet(set, startString) {
    if (!startString || typeof startString !== 'string') {
      return '';
    }
  
    const filter_values = Array.from(set).filter((value) => value.startsWith(startString));
  
    const clean_values = filter_values.map((value) => {
      if (value.startsWith(startString)) {
        return value.replace(new RegExp(`^${startString}`), '');
      }
      return value;
    });
    return clean_values.join('-');
  }