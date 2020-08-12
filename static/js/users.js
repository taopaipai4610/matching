
// $(document.on(イベント名, 対象となる要素, コールバック関数))
$(document).on("change", "#id_image", function(e) {
  // ユーザーのコンピュータで読み込んだファイルを保持しておく
  let reader;
  // ファイルの有無を判定
  if (e.target.files.length) {
    // ファイル操作をしたいときにFileReaderのオブジェクトを作成　以下のイベントを呼ぶ
    reader = new FileReader;
    // ファイルの読み込みが成功したときに発生するイベント
    reader.onload = function(e) {
      let userThumbnail;
      userThumbnail = document.getElementById('thumbnail');
      // display:block;が適用されるためのコード
      $("#userImgPreview").addClass("is-active");
      userThumbnail.setAttribute('src', e.target.result);
    };
    return reader.readAsDataURL(e.target.files[0]);
  }
});