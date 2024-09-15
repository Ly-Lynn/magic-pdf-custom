from loguru import logger

from magic_pdf.libs.MakeContentConfig import DropMode, MakeMode
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
from magic_pdf.rw.AbsReaderWriter import AbsReaderWriter
from magic_pdf.pipe.AbsPipe import AbsPipe
from magic_pdf.user_api import parse_ocr_pdf


class OCRPipe(AbsPipe):

    def __init__(self, pdf_bytes: bytes, model_list: list, image_writer: AbsReaderWriter, is_debug: bool = False):
        super().__init__(pdf_bytes, model_list, image_writer, is_debug)

    def pipe_classify(self):
        pass

    def pipe_analyze(self):
        self.model_list = doc_analyze(self.pdf_bytes, ocr=True)

    def pipe_parse(self):
        self.pdf_mid_data = parse_ocr_pdf(self.pdf_bytes, self.model_list, self.image_writer, is_debug=self.is_debug)

    def pipe_mk_uni_format(self, img_parent_path: str, drop_mode=DropMode.WHOLE_PDF):
        result = super().pipe_mk_uni_format(img_parent_path, drop_mode)
        logger.info("ocr_pipe mk content list finished")
        return result

    def pipe_mk_markdown(self, img_parent_path: str, drop_mode=DropMode.WHOLE_PDF, md_make_mode=MakeMode.MM_MD):
        result = super().pipe_mk_markdown(img_parent_path, drop_mode, md_make_mode)
        logger.info(f"ocr_pipe mk {md_make_mode} finished")
        return result
