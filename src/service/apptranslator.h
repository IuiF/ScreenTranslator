#pragma once

#include <QStringList>

namespace service
{
class AppTranslator
{
public:
  explicit AppTranslator(const QStringList &translationFiles);

  void retranslate(const QString &language = QString());

private:
  QStringList searchPaths() const;
  QStringList translationFiles_;
};

}  // namespace service
