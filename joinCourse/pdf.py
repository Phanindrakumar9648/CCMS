from fpdf import FPDF
import pymysql

def gens():	
	conn=pymysql.connect("localhost","root","","CCMS")
	cur=conn.cursor()
	name="Vinod"
	sql="select*from joincourse_register"
	cur.execute(sql)
	pdf=FPDF()
	for row in cur.fetchall():
		pdf.add_page("a4")
		pdf.set_font('Arial','B',16)
		pdf.ln(70)
		pdf.cell(90, 10, row[1],0,0,"C")
	pdf.output("a.pdf","F")
