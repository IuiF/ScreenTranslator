#include "apptranslator.h"

#include <QApplication>
#include <QLibraryInfo>
#include <QTranslator>

namespace service
{
AppTranslator::AppTranslator(const QStringList &translationFiles)
  : translationFiles_(translationFiles)
{
}

void AppTranslator::retranslate(const QString &language)
{
  auto app = QCoreApplication::instance();
  const auto oldTranslators = app->findChildren<QTranslator *>();
  for (const auto &old : oldTranslators) {
    old->deleteLater();
  }

  const auto files =
      QStringList{QStringLiteral("qt"), QStringLiteral("qtbase")} +
      translationFiles_;
  const auto paths = searchPaths();

  auto last = new QTranslator(app);
  for (const auto &name : files) {
    for (const auto &path : paths) {
      bool loaded = false;
      if (language.isEmpty()) {
        loaded = last->load(QLocale(), name, QLatin1String("_"), path);
      } else {
        // Try language code directly first (e.g., "screentranslator_ja")
        loaded = last->load(name + "_" + language, path);
        // If that fails, try with QLocale
        if (!loaded) {
          loaded = last->load(QLocale(language), name, QLatin1String("_"), path);
        }
      }
      if (!loaded)
        continue;
      app->installTranslator(last);
      last = new QTranslator(app);
      break;
    }
  }
  last->deleteLater();
}

QStringList AppTranslator::searchPaths() const
{
  return QStringList{
      QLibraryInfo::location(QLibraryInfo::TranslationsPath),
#ifdef Q_OS_LINUX
      qgetenv("APPDIR") +
          QLibraryInfo::location(QLibraryInfo::TranslationsPath),  // appimage
#endif  // ifdef Q_OS_LINUX
      {},
      QLatin1String("translations"),
      QLatin1String(":/translations"),
  };
}

}  // namespace service
