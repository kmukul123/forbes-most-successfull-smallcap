
import Quill from 'quill';

let blotsRegistered = false;

export function registerQuillBlots() {
  if (blotsRegistered) {
    return;
  }

  const Inline = Quill.import('blots/inline') as any; // Cast to any to avoid type errors

  class PositiveBlot extends Inline {
    static blotName = 'positive';
    static tagName = 'span';
    static className = 'positive';
  }

  class NegativeBlot extends Inline {
    static blotName = 'negative';
    static tagName = 'span';
    static className = 'negative';
  }

  class HighlightBlot extends Inline {
    static blotName = 'highlight';
    static tagName = 'span';
    static className = 'highlight';
  }

  Quill.register({ 
    'formats/positive': PositiveBlot, 
    'formats/negative': NegativeBlot, 
    'formats/highlight': HighlightBlot 
  });

  blotsRegistered = true;
}
