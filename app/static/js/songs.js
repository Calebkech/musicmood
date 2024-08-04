$(document).ready(function () {
    // Handle delete button click to show modal
    $('.delete-song-btn').on('click', function () {
        var songId = $(this).data('song-id');
        $('#modalSongId').val(songId);
    });

    // Close modal and clear the song ID
    $('#deleteModal').on('hidden.bs.modal', function () {
        $('#modalSongId').val('');
    });
});
