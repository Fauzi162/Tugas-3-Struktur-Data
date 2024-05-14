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

routes = {}

        for city in unvisited_cities:
            distances[city] = float("inf")
        distances[kota_awal] = 0
        
        
        while unvisited_cities:
            closest_city = None
            for city in unvisited_cities:
                if closest_city == None:
                    closest_city = city
                elif distances[city] < distances[closest_city]:
                    closest_city = city
                    
            for neighbour, distance in self.daftarKota[closest_city].items():
                total_distance = round(distances[closest_city] + distance, 1)
                if total_distance < distances[neighbour]:
                    distances[neighbour] = total_distance
                    routes[neighbour] = closest_city

            unvisited_cities.remove(closest_city)

        del distances[kota_awal]
        return distances, routes 


petaJepang = Peta()
petaJepang.tambahKota("Mori")
petaJepang.tambahKota("Iwata")
petaJepang.tambahKota("Fukuroi")
petaJepang.tambahKota("Kakegawa")
petaJepang.tambahKota("Kikugawa")
petaJepang.tambahKota("Shimada")
petaJepang.tambahKota("Fujieda")
petaJepang.tambahKota("Yaizu")
