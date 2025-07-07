
import Quill from 'quill';

let blotsRegistered = false;

export function registerQuillBlots() {
  if (blotsRegistered) {
    return;
  }

  const Inline = Quill.import('blots/inline') as any;

  // Define custom blots for text formatting
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

  // Define custom font sizes
  const Size = Quill.import('attributors/style/size') as any;
  const allowedSizes = ['10px', '12px', '14px', '16px', '18px', '20px', '24px', '36px'];
  Size.whitelist = allowedSizes;

  Quill.register({
    'formats/positive': PositiveBlot,
    'formats/negative': NegativeBlot,
    'formats/highlight': HighlightBlot,
    'attributors/style/size': Size
  }, true);

  blotsRegistered = true;
}
