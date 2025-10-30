# image_utils.py
from PIL import Image
import pytesseract
import io

# Optional: we attempt to use a small huggingface image-captioning model if available.
try:
    from transformers import BlipProcessor, BlipForConditionalGeneration
    _HAS_BLIP = True
except Exception:
    _HAS_BLIP = False

_caption_model = None
_caption_processor = None

if _HAS_BLIP:
    try:
        _caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    except Exception:
        _HAS_BLIP = False


def caption_image(pil_image: Image.Image) -> str:
    """Return a short caption for the PIL image. Falls back to empty string if model not present."""
    if not _HAS_BLIP or _caption_model is None:
        return ""

    inputs = _caption_processor(pil_image, return_tensors="pt")
    out = _caption_model.generate(**inputs)
    caption = _caption_processor.decode(out[0], skip_special_tokens=True)
    return caption


def ocr_image(pil_image: Image.Image) -> str:
    """Run OCR using pytesseract and return extracted text."""
    try:
        text = pytesseract.image_to_string(pil_image)
        return text.strip()
    except Exception:
        return ""
