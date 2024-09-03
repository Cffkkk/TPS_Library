import streamlit as st
import pandas as pd
import datetime
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder
from st_aggrid.shared import JsCode

st.set_page_config(layout='wide')

st.title("Terpene Synthase-standard Library")

now = datetime.datetime.now()
current_hour = now.hour

if 5 <= current_hour < 12:
    st.write("### Good morning!")
elif 12 <= current_hour < 18:
    st.write("### Good afternoon!")
elif 18 <= current_hour < 22:
    st.write("### Good evening!")
else:
    st.write("### It's late, time to rest!")

file_path = 'output.csv'
df = pd.read_csv(file_path)

# 定义AG-Grid的列配置
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination()

# 自定义cellRenderer来显示超链接
cell_renderer = JsCode("""
    class LinkCellRenderer {
      init(params) {
        this.eGui = document.createElement('div');
        this.eGui.innerHTML = params.value;
        this.eGui.style.cursor = 'pointer';
      }
      getGui() {
        return this.eGui;
      }
    }
""")

# 配置列以使用自定义的cellRenderer
gb.configure_column(
    "Link",
    headerName="Link",
    cellRenderer=cell_renderer
)

# 创建AG-Grid表格
AgGrid(df,
    gridOptions=gb.build(),
    updateMode=GridUpdateMode.VALUE_CHANGED,
    allow_unsafe_jscode=True,
    height=625, size=10
)

st.write("1. Ye, Z., et al., CouPling cell growth and biochemical Pathway induction in Saccharomyces cerevisiae for Production of (+)-valencene and its chemical conversion to (+)-nootkatone. Metabolic Engineering, 2022. 72: P. 107-115.\n"
         "2. Deng, X., et al., Systematic identification of Ocimum sanctum sesquiterPenoid synthases and (−)-eremoPhilene overProduction in engineered yeast. Metabolic Engineering, 2022. 69: P. 122-133.\n"
         "3. Quin, M.B., S.N. Michel, and C. Schmidt‐Dannert, Moonlighting Metals: Insights into Regulation of Cyclization Pathways in Fungal Δ6‐Protoilludene SesquiterPene Synthases. ChemBioChem, 2015. 16(15): P. 2191-2199.\n"
         "4. Chen, R., et al., Characterization of tremulane sesquiterPene synthase from the basidiomycete IrPex lacteus. Organic Letters, 2022. 24(31): P. 5669-5673.\n"
         "5. Burkhardt, I., et al., Mechanistic characterization of three sesquiterPene synthases from the termite-associated fungus Termitomyces. Organic & Biomolecular Chemistry, 2019. 17(13): 3348-3355.")
