import tkinter as tk


class MapaConceptualApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Actividad 4 - Mapa Conceptual: Circuitería Alternativa y E/S")
        self.root.geometry("1280x800")
        self.root.configure(bg="#f8f9fa")

        # Contenedor principal para Canvas y Scrollbar
        main_frame = tk.Frame(self.root, bg="#f8f9fa")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(main_frame, bg="#f8f9fa", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.dibujar_mapa()

    def crear_nodo(self, x, y, texto, bg_color="#2f3640", fg_color="white", w=220, h=65):
        """Dibuja un rectángulo con bordes redondeados y texto centrado."""
        x1, y1 = x - w // 2, y - h // 2
        x2, y2 = x + w // 2, y + h // 2

        # Sombra del cuadro
        self.canvas.create_rectangle(x1 + 3, y1 + 3, x2 + 3, y2 + 3, fill="#dcdde1", outline="")

        # Cuadro principal
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline="#718093", width=2)
        self.canvas.create_text(x, y, text=texto, fill=fg_color, font=("Segoe UI", 9, "bold"), justify=tk.CENTER)

        return (x, y, h)

    def conectar(self, origen, destino):
        """Conecta dos nodos mediante una línea flecha limpia."""
        x_orig, y_orig, h_orig = origen
        x_dest, y_dest, h_dest = destino

        p1 = (x_orig, y_orig + (h_orig // 2))
        p2 = (x_dest, y_dest - (h_dest // 2))

        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="#7f8c8d", width=2, arrow=tk.LAST)

    def dibujar_mapa(self):
        # -------------------------------------------------------------
        # NIVEL 1: Raíz Principal (Centro Superior)
        # -------------------------------------------------------------
        raiz = self.crear_nodo(640, 50, "ARQUITECTURA DE COMPUTADORAS\nY SISTEMAS DE E/S", "#1e3799", w=320, h=55)

        # -------------------------------------------------------------
        # NIVEL 2: Ramas Principales
        # -------------------------------------------------------------
        sub1 = self.crear_nodo(300, 160, "1. CIRCUITERÍA ALTERNATIVA", "#0c2461", w=240, h=45)
        sub2 = self.crear_nodo(980, 160, "2. ENTRADA / SALIDA (E/S)", "#0c2461", w=240, h=45)

        self.conectar(raiz, sub1)
        self.conectar(raiz, sub2)

        # -------------------------------------------------------------
        # NIVEL 3: Desglose Circuitería Alternativa (Lado Izquierdo)
        # -------------------------------------------------------------
        c1 = self.crear_nodo(160, 300,
                             "DEFINICIÓN:\nBloques lógicos auxiliares\nque complementan a la CPU\npara optimizar el tráfico.",
                             "#4a69bd", w=220, h=75)
        c2 = self.crear_nodo(440, 300,
                             "COMPONENTES CLAVE:\n• Encoders / Decoders\n• Registros de desplazamiento\n• Buffers Tri-state\n• Módulos de temporización",
                             "#4a69bd", w=220, h=85)

        self.conectar(sub1, c1)
        self.conectar(sub1, c2)

        # -------------------------------------------------------------
        # NIVEL 3: Desglose Entrada / Salida (Lado Derecho)
        # -------------------------------------------------------------
        e1 = self.crear_nodo(720, 290,
                             "DEFINICIÓN:\nInterfaz que gestiona la\ncomunicación entre el\nprocesador y periféricos.",
                             "#4a69bd", w=200, h=75)
        e2 = self.crear_nodo(950, 290, "MAPEO DE MEMORIA", "#10ac84", w=180, h=45)
        e3 = self.crear_nodo(1160, 290, "TÉCNICAS DE\nTRANSFERENCIA", "#10ac84", w=160, h=45)

        self.conectar(sub2, e1)
        self.conectar(sub2, e2)
        self.conectar(sub2, e3)

        # -------------------------------------------------------------
        # NIVEL 4: Detalles de Mapeo de Memoria
        # -------------------------------------------------------------
        m1 = self.crear_nodo(840, 440,
                             "E/S Mapeada en Memoria:\nComparten el mismo espacio\nde direcciones que la RAM.",
                             "#78e08f", fg_color="black", w=200, h=70)
        m2 = self.crear_nodo(1060, 440,
                             "E/S Mapeada en Puertos:\nEspacio y comandos aislados\n(Instrucciones IN / OUT).",
                             "#78e08f", fg_color="black", w=200, h=70)

        self.conectar(e2, m1)
        self.conectar(e2, m2)

        # -------------------------------------------------------------
        # NIVEL 4: Detalles de Técnicas de Transferencia
        # -------------------------------------------------------------
        t1 = self.crear_nodo(780, 600,
                             "E/S Programada:\nLa CPU consulta\ncontinuamente el estado\ndel periférico (Polling).",
                             "#b8e994", fg_color="black", w=190, h=75)
        t2 = self.crear_nodo(990, 600,
                             "E/S por Interrupciones:\nEl periférico notifica\na la CPU cuando está listo\npara operar.",
                             "#b8e994", fg_color="black", w=190, h=75)
        t3 = self.crear_nodo(1190, 600,
                             "Acceso Directo (DMA):\nEl controlador transfiere\ndatos a memoria sin pasar\npor la CPU.",
                             "#b8e994", fg_color="black", w=180, h=75)

        self.conectar(e3, t1)
        self.conectar(e3, t2)
        self.conectar(e3, t3)


if __name__ == "__main__":
    root = tk.Tk()
    app = MapaConceptualApp(root)
    root.mainloop()