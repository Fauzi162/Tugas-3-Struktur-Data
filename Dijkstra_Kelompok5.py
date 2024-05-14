class Peta:
    def _init_(self):
        self.daftarKota = {}
    
    def tambahKota(self, kota):
        if kota not in self.daftarKota:
            self.daftarKota[kota] = {}
    
    def printKota(self):
        for kota in self.daftarKota:
            print(f"{kota}")
            for kotaTetangga, jarak in self.daftarKota[kota].items():
                print(f"--> {kotaTetangga} km -- {jarak}")
    
    def tambahJarak(self, kota1, kota2, jarak):
        if kota1 and kota2 in self.daftarKota:
            self.daftarKota[kota1][kota2] = jarak
            self.daftarKota[kota2][kota1] = jarak
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.daftarKota:
            for kota in self.daftarKota:
                if kotaDihapus in self.daftarKota[kota]:
                    del self.daftarKota[kota][kotaDihapus]
            del self.daftarKota[kotaDihapus]
    
    def hapusJarak(self, kota1, kota2):
        if kota1 and kota2 in self.daftarKota:
            del self.daftarKota[kota1][kota2]
            del self.daftarKota[kota2][kota1]


    def dijkstra(self, kota_awal):
        
        unvisited_cities = [*self.daftarKota.keys()]
        distances = {}
