import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

FONT_NAME = "Times New Roman"
COLOR_PRIMARY = RGBColor(0x1F, 0x49, 0x7D)  # Navy Blue
COLOR_TEXT = RGBColor(0x11, 0x18, 0x27)     # Dark Charcoal
COLOR_MUTED = RGBColor(0x4B, 0x55, 0x63)    # Muted Gray

def set_run_font(run, name=FONT_NAME, size_pt=12, bold=False, italic=False, color=COLOR_TEXT):
    run.font.name = name
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    # Ensure East Asian and Complex Script font names are also set for Word consistency
    rPr = run._r.get_or_add_rPr()
    rFonts = OxmlElement('w:rFonts')
    rFonts.set(qn('w:ascii'), name)
    rFonts.set(qn('w:hAnsi'), name)
    rFonts.set(qn('w:cs'), name)
    rPr.append(rFonts)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_border(cell, **kwargs):
    """
    kwargs can be top, bottom, left, right.
    values like: {"sz": 4, "val": "single", "color": "CBD5E1"}
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        if border_name in kwargs:
            b = OxmlElement(f'w:{border_name}')
            for key, val in kwargs[border_name].items():
                b.set(qn(f'w:{key}'), str(val))
            tcBorders.append(b)
        else:
            b = OxmlElement(f'w:{border_name}')
            b.set(qn('w:val'), 'none')
            tcBorders.append(b)
    tcPr.append(tcBorders)

def add_chapter_heading(doc, chapter_num_str, title_str):
    """
    Times New Roman, 20 pt, Bold, ALL CAPS, Center aligned
    Example:
    CHAPTER 1
    PRELIMINARY INVESTIGATION
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    run1 = p.add_run(chapter_num_str.upper())
    set_run_font(run1, name=FONT_NAME, size_pt=20, bold=True, color=COLOR_PRIMARY)
    
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(20)
    p2.paragraph_format.line_spacing = 1.0
    run2 = p2.add_run(title_str.upper())
    set_run_font(run2, name=FONT_NAME, size_pt=20, bold=True, color=COLOR_PRIMARY)

def add_section_heading(doc, num_str, title_str):
    """
    Times New Roman, 14 pt, Bold, Left aligned
    Example: 1.1 Organizational Overview
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    full_text = f"{num_str} {title_str}" if num_str else title_str
    run = p.add_run(full_text)
    set_run_font(run, name=FONT_NAME, size_pt=14, bold=True, color=COLOR_PRIMARY)

def add_subsection_heading(doc, num_str, title_str):
    """
    Times New Roman, 12 pt, Bold, Left aligned
    Example: 1.1.1 Background of the System
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    full_text = f"{num_str} {title_str}" if num_str else title_str
    run = p.add_run(full_text)
    set_run_font(run, name=FONT_NAME, size_pt=12, bold=True, color=RGBColor(0x1F, 0x29, 0x37))

def add_subsubsection_heading(doc, title_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    run = p.add_run(title_str)
    set_run_font(run, name=FONT_NAME, size_pt=12, bold=True, italic=True, color=RGBColor(0x37, 0x41, 0x51))

def add_body_p(doc, text):
    """
    Times New Roman, 12 pt, Single spacing, Justified
    """
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(text)
    set_run_font(run, name=FONT_NAME, size_pt=12, bold=False, color=COLOR_TEXT)
    return p

def add_bullet_p(doc, bold_prefix, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.left_indent = Inches(0.25)
    
    run_bullet = p.add_run("▪  ")
    set_run_font(run_bullet, name=FONT_NAME, size_pt=10, bold=True, color=COLOR_PRIMARY)
    
    if bold_prefix:
        run_bold = p.add_run(bold_prefix + ": ")
        set_run_font(run_bold, name=FONT_NAME, size_pt=12, bold=True, color=COLOR_TEXT)
        
    run_text = p.add_run(text)
    set_run_font(run_text, name=FONT_NAME, size_pt=12, bold=False, color=COLOR_TEXT)
    return p

def add_numbered_p(doc, num_str, bold_prefix, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.left_indent = Inches(0.25)
    
    run_num = p.add_run(f"{num_str}. ")
    set_run_font(run_num, name=FONT_NAME, size_pt=12, bold=True, color=COLOR_PRIMARY)
    
    if bold_prefix:
        run_bold = p.add_run(bold_prefix + ": ")
        set_run_font(run_bold, name=FONT_NAME, size_pt=12, bold=True, color=COLOR_TEXT)
        
    run_text = p.add_run(text)
    set_run_font(run_text, name=FONT_NAME, size_pt=12, bold=False, color=COLOR_TEXT)
    return p

def add_code_block(doc, code_str, caption=None):
    if caption:
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_cap.paragraph_format.space_before = Pt(8)
        p_cap.paragraph_format.space_after = Pt(3)
        p_cap.paragraph_format.keep_with_next = True
        r = p_cap.add_run(caption)
        set_run_font(r, name=FONT_NAME, size_pt=10.5, bold=True, italic=True, color=COLOR_MUTED)
        
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.25)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
    cell._tc.get_or_add_tcPr().append(shd)
    border_kwargs = {
        'top': {'sz': 4, 'val': 'single', 'color': 'CBD5E1'},
        'bottom': {'sz': 4, 'val': 'single', 'color': 'CBD5E1'},
        'left': {'sz': 12, 'val': 'single', 'color': '1F497D'},
        'right': {'sz': 4, 'val': 'single', 'color': 'CBD5E1'}
    }
    set_cell_border(cell, **border_kwargs)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    run = p.add_run(code_str)
    set_run_font(run, name="Consolas", size_pt=9.5, bold=False, color=RGBColor(0x1F, 0x29, 0x37))
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(6)

def add_figure_box(doc, fig_id, fig_title, description_paragraphs, image_path=None):
    """
    Adds a figure block with placeholder or image, caption, and academic technical explanation.
    """
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.25)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>')
    cell._tc.get_or_add_tcPr().append(shd)
    
    border_kwargs = {
        'top': {'sz': 6, 'val': 'dashed', 'color': '94A3B8'},
        'bottom': {'sz': 6, 'val': 'dashed', 'color': '94A3B8'},
        'left': {'sz': 6, 'val': 'dashed', 'color': '94A3B8'},
        'right': {'sz': 6, 'val': 'dashed', 'color': '94A3B8'}
    }
    set_cell_border(cell, **border_kwargs)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    
    if image_path:
        try:
            p.add_run().add_picture(image_path, width=Inches(3.5))
        except Exception:
            run_ph = p.add_run(f"[{fig_id} — {fig_title.upper()}]")
            set_run_font(run_ph, name=FONT_NAME, size_pt=11, bold=True, color=COLOR_PRIMARY)
    else:
        run_ph = p.add_run(f"[INSERT {fig_id.upper()} — {fig_title.upper()} HERE]")
        set_run_font(run_ph, name=FONT_NAME, size_pt=11, bold=True, color=COLOR_PRIMARY)
        
    # Caption
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(6)
    p_cap.paragraph_format.space_after = Pt(6)
    p_cap.paragraph_format.keep_with_next = True
    r_cap = p_cap.add_run(f"{fig_id} — {fig_title}")
    set_run_font(r_cap, name=FONT_NAME, size_pt=11, bold=True, color=COLOR_PRIMARY)
    
    # Technical explanation
    p_exp_hdr = doc.add_paragraph()
    p_exp_hdr.paragraph_format.space_before = Pt(4)
    p_exp_hdr.paragraph_format.space_after = Pt(2)
    p_exp_hdr.paragraph_format.keep_with_next = True
    r_hdr = p_exp_hdr.add_run(f"Technical Explanation for {fig_id}:")
    set_run_font(r_hdr, name=FONT_NAME, size_pt=11.5, bold=True, italic=True, color=COLOR_PRIMARY)
    
    for para in description_paragraphs:
        add_body_p(doc, para)

def add_styled_table(doc, table_id, table_title, headers, data, col_widths=None):
    """
    Creates a professionally styled table with header and alternating row colors.
    """
    p_cap = doc.add_paragraph()
    p_cap.paragraph_format.space_before = Pt(10)
    p_cap.paragraph_format.space_after = Pt(4)
    p_cap.paragraph_format.keep_with_next = True
    r_cap = p_cap.add_run(f"{table_id}: {table_title}")
    set_run_font(r_cap, name=FONT_NAME, size_pt=11, bold=True, color=COLOR_PRIMARY)
    
    num_rows = len(data) + 1
    num_cols = len(headers)
    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Header row
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="1F497D"/>')
        hdr_cells[i]._tc.get_or_add_tcPr().append(shd)
        set_cell_margins(hdr_cells[i], top=80, bottom=80, left=100, right=100)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        for r in p.runs:
            set_run_font(r, name=FONT_NAME, size_pt=10.5, bold=True, color=RGBColor(255, 255, 255))
            
    # Data rows
    for r_idx, row_values in enumerate(data):
        row_cells = table.rows[r_idx + 1].cells
        fill_color = "FFFFFF" if r_idx % 2 == 0 else "F8FAFC"
        for c_idx, val in enumerate(row_values):
            row_cells[c_idx].text = str(val)
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
            row_cells[c_idx]._tc.get_or_add_tcPr().append(shd)
            set_cell_margins(row_cells[c_idx], top=70, bottom=70, left=100, right=100)
            
            border_kwargs = {
                'top': {'sz': 4, 'val': 'single', 'color': 'E2E8F0'},
                'bottom': {'sz': 4, 'val': 'single', 'color': 'E2E8F0'},
                'left': {'sz': 4, 'val': 'single', 'color': 'E2E8F0'},
                'right': {'sz': 4, 'val': 'single', 'color': 'E2E8F0'}
            }
            set_cell_border(row_cells[c_idx], **border_kwargs)
            
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            for r in p.runs:
                set_run_font(r, name=FONT_NAME, size_pt=10, bold=False, color=COLOR_TEXT)
                
    # Column widths
    if col_widths and len(col_widths) == num_cols:
        for row in table.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)
                
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(6)

def add_callout_box(doc, title, text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    cell.width = Inches(6.25)
    set_cell_margins(cell, top=90, bottom=90, left=140, right=140)
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EFF6FF"/>')
    cell._tc.get_or_add_tcPr().append(shd)
    
    border_kwargs = {
        'top': {'sz': 4, 'val': 'single', 'color': 'BFDBFE'},
        'bottom': {'sz': 4, 'val': 'single', 'color': 'BFDBFE'},
        'left': {'sz': 16, 'val': 'single', 'color': '2563EB'},
        'right': {'sz': 4, 'val': 'single', 'color': 'BFDBFE'}
    }
    set_cell_border(cell, **border_kwargs)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    r_title = p.add_run(f"📌 {title}\n")
    set_run_font(r_title, name=FONT_NAME, size_pt=11, bold=True, color=RGBColor(0x1E, 0x40, 0xAF))
    
    r_text = p.add_run(text)
    set_run_font(r_text, name=FONT_NAME, size_pt=10.5, italic=False, color=RGBColor(0x1E, 0x3A, 0x8A))
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(2)
    p_after.paragraph_format.space_after = Pt(6)

def add_page_number_field(run):
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = "PAGE"
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    r = run._r
    r.append(fldChar1)
    r.append(instrText)
    r.append(fldChar2)
    r.append(fldChar3)
