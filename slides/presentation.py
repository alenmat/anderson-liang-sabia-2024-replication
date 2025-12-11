from fpdf import FPDF
from io import BytesIO
from matplotlib.figure import Figure

# Unb Colors - RGB(0,51,102) and RGB(0,102,51)

class PDF(FPDF):
    def __init__(self, unit='mm', format=(190.5,338.7)):
        super().__init__(orientation='L', unit=unit, format=format)

    def header(self):
        self.set_font('Helvetica', style='', size=12)
        col_width = (self.w - self.l_margin - self.r_margin) / 2
        pdf.set_draw_color(r=0, g=51, b=102)
        self.line(self.l_margin, 18, self.w - self.r_margin, 18)
        pdf.set_text_color(r=0, g=51, b=102)
        self.cell(col_width, 10, 'CPPGA3254 - Econometria I', border=0, align='L', ln=0)
        self.image('images/as_bas_cor.jpg', x =(self.w - 25) / 2, y = 9, w=25)
        self.cell(col_width, 10, 'Exercício Empírico', border=0, align='R', ln=0)
        self.ln(20)


    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 10)
        pdf.set_text_color(r=0, g=51, b=102)
        self.cell(0, 10, 'Matheus Alencastro - 251100926 ', 0, 0, 'C')
        self.cell(0, 10, f'{self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)

WIDTH = (pdf.w - pdf.l_margin - pdf.r_margin)

# -- TITLE SLIDE --
pdf.add_page()
pdf.set_font("Helvetica", "B", 24)
pdf.set_y(60)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Mandatory seatbelt laws and traffic fatalities: A reassessment',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=20)
pdf.set_text_color(r=77, g=77, b=77)
pdf.cell(0,10,' D. Mark Anderson, Yang Liang, and Joseph J. Sabia (2024)',align='C')
pdf.ln(20)
pdf.cell(0,10,'Journal of Applied Econometrics',align='C')

# -- SLIDE 1 -- Referência e motivação
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Referência e Motivação',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - [Anderson, D. M., Liang, Y., & Sabia, J. J. (2024). Mandatory seatbelt laws and traffic fatalities: A reassessment. Journal of Applied Econometrics, 39(3), 513-521](https://doi.org/10.1002/jae.3026).''', 
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - [Os dados e o código em Stata](https://journaldata.zbw.eu/dataset/b5f4c0f6-dd9e-4cdc-bea4-04a7efdb50dd/resource/98aa0a14-b449-46b4-8cac-23a1ef0094fd) foram disponibilizados pelos autores.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - O artigo busca revisar a estimação feita por [Cohen e Einav (2003)](https://doi.org/10.1162/003465303772815754) que apontava que as leis de uso de cinto de segurança nos Estados Unidos estavam associadas com uma redução entre 4 e 6% dos acidentes com fatalidades.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Neste artigo de 2003 a estimação foi feita a partir do que se conhece como Difference-in-Differences (DiD), mais especificamente por meio de Two-Way Fixed Effects (TWFE).''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Nesse sentido, a motivação para a escolha do artigo foi a possibilidade de ter contato com essa técnica e procurar fazer uma estimação do tipo DiD TWFE.''',
    markdown=True
    )

# -- SLIDE 2 -- Base econômica para o material discutido no artigo (revisão da literatura)
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Base Teórica',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Anderson et al. (2024) apresentam uma extensão da análise realizada por Cohen e Einav (2003). No artigo, os autores replicam as estimativas do estudo original, aumentam a janela temporal de análise (antes 1983-1997, depois 1983-2019), aplicam o estimador __Interaction Weighted__ proposto por Sun e Abraham (2021) e estimam modelos do tipo __event study__.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Do ponto de vista econométrico, o estudo avança no sentido de restimar o modelo TWFE aplicado originalmente, que, conforme mostrado por Goodman-Bacon (2021), pode estar viesado caso os efeitos das leis de uso de cinto de segurança forem dinâmicos e heterogêneos. Por exemplo, a aprovação de leis que determinam uso de cinto obrigatório pode provocar uma mudança no senso de segurança e no comportamento de dirigir do motorista, fazendo com que este assuma uma postura mais arriscada no trânsito (Efeito Peltzman).''',
    markdown=True
    )

# -- SLIDE 3 -- Detalhamento da base de dados
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Detalhamento da Base de Dados e Especificação do Modelo',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=14)
pdf.set_text_color(r=77, g=77, b=77)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - **__Primary Seatbelt Laws (PSL):__** Permitem aos oficiais da lei parar veículos e multar os que estiverem sem cinto independente de outro tipo de conduta do motorista.''',
    markdown=True
    )
pdf.ln(.1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - **__Secondary Seatbelt Laws (SSL):__** Permitem aos oficiais da lei multar infratores que não estiverem usando cinto apenas se tiverem sido parados por outro tipo de ofensa.''',
    markdown=True
    )
pdf.ln(.1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - **__Occupant fatalities:__** é a taxa de fatalidades dos passageiros no trânsito por milhas viajadas (__vehicle miles traveled - VMT__).''',
    markdown=True
    )
pdf.ln(.1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - **Variáveis de controle:** __%Black__, __%Hispanic__, __Mean Age__, __Median Income__, __Unemployment__, __Violent Crime__, __Property Crime__, __Rural Traffic Density__, __Urban Traffic Density__, __Rural VMT__, __Urban VMT__, __Fuel Tax__, __65 MPH Limit__, __70+ MPH Limit__, __BAC 0.08__, __MLDA 21__.''',
    markdown=True
    )
pdf.ln(.1)

fig1 = Figure(figsize=(6,2))
gca = fig1.gca()
gca.text(0, 0.5, r"$Occupant\:fatalities_{st} = \beta_0 + \beta_1 SSL_{st} + \beta_2 PSL_{st} + \beta_3 SSLtoPSL_{st} + \mathbf{X_{st}' \beta_4} + \alpha_{s} + \tau_{t} + \varepsilon_{st}$", fontsize=20)
gca.axis('off')

img = BytesIO()
fig1.savefig(img, format='svg')

pdf.image(img, x=45, y=137, w=120)

# -- SLIDE 4 -- Algum detalhe ou estatística que você pretende discutir usando os dados reais
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Resultados dos Autores',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)
pdf.image('images/table_1.png', x= 45, y=45, w=250)

# -- SLIDE 5 -- Tabela com os resultados econométricos
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Exercício Empírico',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)

fig2 = Figure(figsize=(6,2))
gca = fig2.gca()
gca.text(0, 0.5, r"$Occupant\:fatalities_{st} = \beta_0 + \sum_{e \in E}\sum_{l=-4, l\ne-1}^{4} \delta_{e,l} \cdot 1(Cohort_s = e) \cdot 1(Year_t - e = l) + \mathbf{X_{st}' \beta_4} + \alpha_{s} + \tau_{t} + \varepsilon_{st}$", fontsize=20)
gca.axis('off')

img = BytesIO()
fig2.savefig(img, format='svg')

pdf.image(img, x=25, y=40, w=120)

pdf.image('images/output_table.png', x= 60, y=75, w=220)

# -- SLIDE 6 -- Alguma Figura que represente os dados
pdf.add_page()
pdf.image('images/output_plot.png', x= 50, y=25, w=220)


# -- SLIDE 7 -- Código que você desenvolveu para fazer o exercício
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Código',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - O código para a estimação do modelo DiD TWFE robusto a heterogeneidades temporais conforme proposto por Sun e Abraham (2021) pode ser consultado no meu [GitHub](https://github.com/alenmat/anderson-liang-sabia-2024-replication/blob/main/main.ipynb). O código foi desenvolvido usando Python (3.11) e sua apresentação foi feita em um Jupyter Notebook (arquivo __main.ipynb__). ''',
    markdown=True
    )
pdf.image('images/GitHub-Logo.png', x = 127, y = 100, w=80, link='https://github.com/alenmat/anderson-liang-sabia-2024-replication/blob/main/main.ipynb')

# -- SLIDE 8 -- Conclusão
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Conclusão',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Os resultados alcançados pelos autores são consistentes com aqueles apresentados por Cohen e Einav (2003).''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Compete destacar que o artigo avança em apontar para a robustez dos efeitos das PSLs na redução da fatalidade dos ocupantes.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Já no que tange às SSLs, os efeitos dependem da escolha funcional do modelo. Este resultado é surpreendente uma vez que a literatura passada considerava as SSLs como uma ferramenta efetiva de redução de fatalidades entre os ocupantes de veículos.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    - Finalmente, ainda é possível inferir que não há evidências de que as leis de uso de cinto de segurança são positivamente correlacionadas com os acidentes envolvendo não ocupantes. Portanto, trata-se de um argumento contrário a teoria desenvolvida por Peltzman.''',
    markdown=True
    )

# -- SLIDE 9 -- Referëncias
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(r=0, g=102, b=51)
pdf.cell(0,10,'Referências',align='C')
pdf.ln(20)
pdf.set_font("Helvetica", size=16)
pdf.set_text_color(r=77, g=77, b=77)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    Anderson, D. M., Liang, Y., & Sabia, J. J. (2024). Mandatory seatbelt laws and traffic fatalities: A reassessment. Journal of Applied Econometrics, 39(3), 513~521. https://doi.org/10.1002/jae.3026''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    Cohen, A., & Einav, L. (2003). The effects of mandatory seat belt laws on driving behavior and traffic fatalities. Review of Economics and Statistics, 85(4), 828~843. https://doi.org/10.1162/003465303772815754''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Journal of Econometrics, 225(2), 254~277. https://doi.org/10.1016/j.jeconom.2021.03.014.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    Matheus Facure, "The Diff-in-Diff Saga," in Causal Inference for the Brave and True, accessed [Dec. 2025], https://matheusfacure.github.io/python-causality-handbook/24-The-Diff-in-Diff-Saga.html.''',
    markdown=True
    )
pdf.ln(1)
pdf.multi_cell(
    w= WIDTH,
    h=8,
    text='''
    Sun, L., & Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. Journal of Econometrics, 225(2), 175~199. https://doi.org/10.1016/j.jeconom.2020.09.006''',
    markdown=True
    )
pdf.ln(1)


def create_slides():
    pdf.output("presentation.pdf")
    print("Slides created successfully!")

if __name__ == "__main__":
    create_slides()