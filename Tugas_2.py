from z3 import *

A, T, S, J, I, P, C, D, E, U, K, B, M, L = Bools(
  "memiliki_kartu_akses_aktif " # A
  "menyelesaikan_pelatihan_keselamatan " # T
  "sedang_terkena_sanksi " # S
  "Jam_kerja_normal " # J
  "Mendapat_izin_khusus " # I
  "Supervisor_berada_di_lokasi " # P
  "Memiliki_sertifikasi_khusus_alat " # C
  "Sistem_mendeteksi_kondisi_darurat " # D
  "Menggunakan_peralatan_berisiko_tinggi " # E
  "Menggunakan_peralatan_lab_(biasa) " # U
  "Kartu_akses_kedaluwarsa " # K
  "Adanya_petugas_keselamatan " # B
  "Memperoleh_emergency_access " # M
  "Memperoleh_akses_masuk_ke_lab"
)

solver = Solver()

solver.add(Implies(L, A))
solver.add(Implies(L, T))
solver.add(Implies(S, Not(L)))
solver.add(Implies(And(J, A, T, Not(S), Not(D)), L))
solver.add(Implies(And(Not(J), L), I))
solver.add(Implies(And(Not(J), L), P))
solver.add(Implies(E, C))
solver.add(Implies(E, P))
solver.add(Implies(D, Not(L)))
solver.add(Implies(And(D, B), M))
solver.add(Implies(K, Not(L)))
solver.add(Implies(Not(T), Not(U), Not(E)))
solver.add(Implies(And(L, Not(C)), Not(E)))
solver.add(Implies(U, L))

solver.add(A, T, Not(S), Not(J), I)
print(solver.check())
print(solver.model())