import bpy
import bmesh

def select_faces_with_same_vertices():
    # Dapatkan objek aktif
    obj = bpy.context.active_object
    
    # Pastikan objek adalah mesh
    if obj is None or obj.type != 'MESH':
        print("Silakan pilih objek mesh terlebih dahulu.")
        return
    
    # Masuk ke mode edit
    if bpy.context.mode != 'EDIT_MESH':
        bpy.ops.object.mode_set(mode='EDIT')
    
    # Buat bmesh dari mesh aktif
    bm = bmesh.from_edit_mesh(obj.data)
    
    # Dapatkan semua face yang terpilih
    selected_faces = [f for f in bm.faces if f.select]
    
    # Jika tidak ada face yang terpilih, keluar
    if not selected_faces:
        print("Tidak ada face yang terpilih.")
        return
    
    # Kumpulkan semua lokasi vertex dari face yang terpilih
    selected_vertices_locations = set()
    for face in selected_faces:
        for vert in face.verts:
            selected_vertices_locations.add(tuple(vert.co))
    
    # Pilih semua face yang memiliki vertex dengan lokasi yang sama
    for face in bm.faces:
        if all(tuple(v.co) in selected_vertices_locations for v in face.verts):
            face.select = True
    
    # Perbarui mesh
    bmesh.update_edit_mesh(obj.data)
    print("Face dengan vertex di lokasi yang sama telah terpilih.")

# Jalankan fungsi
select_faces_with_same_vertices()
